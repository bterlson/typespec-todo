import { UserJson as User } from "./types/User.js";
import { TodoItemJson as TodoItem } from "./types/TodoItem.js";
import { TodoPageJson as TodoPage } from "./types/TodoPage.js";
import { TodoItemPatchJson as TodoItemPatch } from "./types/TodoItemPatch.js";
import { TodoAttachmentJson as TodoAttachment } from "./types/TodoAttachment.js";
import { PaginationControlsJson as PaginationControls } from "./types/PaginationControls.js";
import { FastifyReply, FastifyRequest } from "fastify";
import { UserCreatedResponseJson } from "./types/UserCreatedResponse.js";
import { randomBytes } from "node:crypto";
import { apply } from "json-merge-patch";

const DEFAULT_LIMIT = 10;

// have to manually do visibility for JSON Schema based
// types.
type UserCreatedResponse = Omit<
  UserCreatedResponseJson,
  "statusCode" | "password"
>;

interface Database {
  users: Map<number, User>;
  items: Map<number, TodoItem>;
  tokens: Map<string, User>;
  attachmentsByItem: Map<number, TodoAttachment[]>;
}

const database: Database = {
  users: new Map(),
  items: new Map(),
  tokens: new Map(),
  attachmentsByItem: new Map()
};
for (let i = 0; i < 100; i++) {
  database.items.set(i, {
    id: i,
    title: `Item ${i}`,
    createdBy: 1,
    createdAt: new Date().toISOString(),
    status: "NotStarted",
    labels: [],
    updatedAt: new Date().toISOString(),
  });
}

function throwError(code: string, message: string): never {
  const error = new Error(message);
  (error as any).code = code;
  throw error;
}

export class Service {
  async Users_create(req: FastifyRequest<{ Body: User }>) {
    const user = req.body;
    const duplicateUser = Array.from(database.users.values()).find(
      (u) => u.username === user.username || u.email === user.email
    );

    if (duplicateUser) {
      throwError(
        "invalid-user",
        "A user with the same username or email already exists"
      );
    }

    const id = database.users.size + 1;
    user.id = id;
    database.users.set(id, user);

    const token = randomBytes(16).toString("base64");
    database.tokens.set(token, user);

    const response: UserCreatedResponse = {
      id,
      username: user.username,
      email: user.email,
      token,
      validated: false
    };

    return response;
  }

  async Users_validate(req: FastifyRequest<{ Querystring: { token: string }}>, res: FastifyReply) {
    const token = req.query.token;
    if (!token) {
      throwError(
        "invalid-user",
        "That token was not found."
      );
    }

    const user = database.tokens.get(token);
    if (!user) {
      throwError(
        "invalid-user",
        "That token was not found."
      );
    }

    user.validated = true;
    res.status(204).send();
  }

  async TodoItems_list(
    req: FastifyRequest<{ Querystring: PaginationControls }>
  ) {
    const limit = Number(req.query.limit) ?? DEFAULT_LIMIT;
    const offset = Number(req.query.offset) ?? 0;

    const itemsIter = database.items.values();
    for (let i = 0; i < offset; i++) {
      itemsIter.next();
    }

    const items = [];
    for (const item of itemsIter) {
      items.push(item);
      if (items.length === limit) {
        break;
      }
    }
    const hasMore = !itemsIter.next().done;
    const page: TodoPage = {
      items,
      pagination: {
        pageSize: items.length,
        totalSize: database.items.size,
        limit,
        offset,
        prevLink:
          offset > 0
            ? `/items?limit=${limit}&offset=${Math.max(offset - limit, 0)}`
            : undefined,
        nextLink: hasMore
          ? `/items?limit=${limit}&offset=${offset + limit}`
          : undefined,
      },
    };
    return page;
  }

  async TodoItems_create(req: FastifyRequest) {
    const body: { item: TodoItem, attachments?: TodoAttachment[] } = req.body as any;
    const { item, attachments } = body;

    item.id = database.items.size;
    item.createdAt = new Date().toISOString();
    item.updatedAt = new Date().toISOString();
    item.createdBy = 1; // todo: implement users
    database.items.set(item.id, item)
    return item;
  }

  async TodoItems_get(req: FastifyRequest<{ Params: { id: number } }>) {
    const id = Number(req.params.id);
    const todoItem = database.items.get(id);

    if (!todoItem) {
      throwError(
        "item-not-found",
        "User was not found"
      );
    }

    return todoItem;
  }

  async TodoItems_update(req: FastifyRequest<{ Params: { id: number } }>) {
    const patch = req.body as TodoItemPatch;
    const id = Number(req.params.id);
    const todoItem = database.items.get(id);

    if (!todoItem) {
      throwError(
        "item-not-found",
        "Todo item was not found"
      );
    }

    apply(todoItem, patch);

    return todoItem;
  }

  async Attachments_list(req: FastifyRequest<{ Params: { itemId: number } }>) {
    console.log([...database.attachmentsByItem.entries()]);
    const items = database.attachmentsByItem.get(Number(req.params.itemId));
    
    return items ?? [];
  }

  async Attachments_createAttachment(req: FastifyRequest<{ Params: { itemId: number } }>) {
    const id = Number(req.params.itemId);
    if (!database.attachmentsByItem.has(id)) {
      database.attachmentsByItem.set(id, []);
    }

    const list = database.attachmentsByItem.get(id)!;
    const attachment: TodoAttachment = req.body as any;
    list.push(attachment as TodoAttachment);
    console.log("List is", list);
    return;
  }
}
