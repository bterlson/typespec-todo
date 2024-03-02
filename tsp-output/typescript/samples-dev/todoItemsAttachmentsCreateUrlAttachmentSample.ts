// Licensed under the MIT license.

import createTodoApplicationClient from "todo-client";
import * as dotenv from "dotenv";

dotenv.config();

/**
 * This sample demonstrates how to call operation CreateUrlAttachment
 *
 * @summary call operation CreateUrlAttachment
 */
async function todoItemsAttachmentsCreateUrlAttachmentSample() {
  const endpoint = "{Your endpoint}";
  const client = createTodoApplicationClient(endpoint, { key: "{Your key}" });
  const itemId = 123;
  const result = await client
    .path("/items/{itemId}/attachments", itemId)
    .post({
      body: {
        contents: {
          filename: "{Your filename}",
          mediaType: "{Your mediaType}",
          contents: "{Your contents}",
        },
      },
      contentType: "application/json",
    });
  console.log(result);
}

async function main() {
  todoItemsAttachmentsCreateUrlAttachmentSample();
}

main().catch(console.error);
