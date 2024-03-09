# TODO CLI Application

This is a CLI (Command Line Interface) application for managing your TODOs. It allows you to list, add, update, and delete TODO items from your terminal.

## Features

- **List TODO Items**: Quickly see all your tasks and their statuses.
- **Add TODO Items**: Easily add new tasks with titles, optional descriptions, and statuses.
- **Update TODO Items**: Update the status of your tasks as you progress.
- **Delete TODO Items**: Remove tasks that are no longer needed.

## Prerequisites

Before you start, ensure you have the following installed:

- Node.js (version 18.x or newer recommended)
- The client code generated, and the service started. See the readme in the root of this repository for more information.

## Usage

From this folder, run:

```bash
npm install
npm run build
```

The cli is now located at `dist/index.js`.

### Commands

- **List TODOs**

  To list all TODO items, use:

  ```bash
  node dist/index.js list
  ```

- **Add a TODO**

  To add a new TODO item, use:

  ```bash
  node dist/index.js add "<title>" [status] [description]
  ```

  Status is optional and can be one of `NotStarted`, `InProgress`, or `Completed`. The default status is `NotStarted`.

- **Update a TODO**

  To update an existing TODO item's status, use:

  ```bash
  node dist/index.js update <id> <status>
  ```

- **Delete a TODO**

  To delete a TODO item, use:

  ```bash
  node dist/index.js delete <id>
  ```
