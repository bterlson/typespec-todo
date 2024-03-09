#!/usr/bin/env node
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import TodoClient from "./generated-client/src/index.js";
import { paginate } from "./paginate.js";

// Example client setup, adjust according to your client library
const todoClient = TodoClient(
  "http://localhost:3000",

  { allowInsecureConnection: true }
);

yargs(hideBin(process.argv))
  .command({
    command: "list",
    describe: "List all TODO items",
    handler: async () => {
      try {
        const response = await todoClient.path("/items").get();

        if (response.status !== "200") {
          console.error("Failed to fetch TODO items:", response.status);
          return;
        }

        const items = paginate(todoClient, response);

        for await (const item of items) {
          console.log(`- [${item.status}] ${item.title}`);
          if (item.description) {
            console.log(`  ${item.description}`);
          }
        }
      } catch (error) {
        console.error("Failed to fetch TODO items:", error);
      }
    },
  })
  .command<{
    title: string;
    description?: string;
    status: "NotStarted" | "InProgress" | "Completed";
  }>(
    "add <title> [status] [description]",
    "Add a new TODO item",
    (yargs) => {
      yargs
        .positional("title", {
          describe: "TODO title",
          type: "string",
        })
        .positional("description", {
          describe: "TODO description",
          type: "string",
          default: "",
        })
        .positional("status", {
          describe: "New status (NotStarted | InProgress | Completed)",
          type: "string",
          choices: ["NotStarted", "InProgress", "Completed"],
          default: "NotStarted",
        });
    },
    async (argv) => {
      try {
        const response = await todoClient.path("/items").post({
          contentType: "application/json",
          body: {       
            item: {
              title: argv.title,
              description: argv.description,
              status: argv.status,
              labels: []
            },
            attachments: []
          },
        });

        if (response.status !== "200") {
          console.error("Failed to add TODO item:", response.status);
          return;
        }
        console.log(`TODO item added: ${response.body.title}`);
      } catch (error) {
        console.error("Failed to add TODO item:", error);
      }
    }
  )
  .command<{ id: number; status?: "NotStarted" | "InProgress" | "Completed" }>(
    "update <id> <status>",
    "Update the status of a TODO item",
    (yargs) => {
      yargs
        .positional("id", {
          describe: "TODO item ID",
          type: "number",
        })
        .positional("status", {
          describe: "New status (NotStarted | InProgress | Completed)",
          type: "string",
          choices: ["NotStarted", "InProgress", "Completed"],
        });
    },
    async (argv) => {
      try {
        const response = await todoClient.path("/items/{id}", argv.id).patch({
          contentType: "application/merge-patch+json",
          body: { status: argv.status },
        });
        if (response.status !== "200") {
          console.error("Failed to update TODO item:", response.status);
          return;
        }
        console.log("TODO item updated:", response.body.title);
      } catch (error) {
        console.error("Failed to update TODO item:", error);
      }
    }
  )
  .command<{ id: number }>(
    "delete <id>",
    "Delete a TODO item",
    (yargs) => {
      yargs.positional("id", {
        describe: "TODO item ID",
        type: "number",
      });
    },
    async (argv) => {
      try {
        const response = await todoClient.path(`/items/{id}`, argv.id).delete();
        if (response.status !== "204") {
          console.error("Failed to delete TODO item:", response.status);
          return;
        }
        console.log("TODO item deleted successfully.");
      } catch (error) {
        console.error("Failed to delete TODO item:", error);
      }
    }
  )
  .demandCommand(1, "You need at least one command before moving on")
  .help().argv;
