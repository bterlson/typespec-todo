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
- [tsx](https://github.com/privatenumber/tsx) for executing TypeScript files directly

## Installation

To use the TODO CLI application, follow these steps:

1. Install the required dependencies:

```bash
npm install
```

2. Build the project

```bash
npm run build
```

3. Start the TODO service

```bash
npm start
```

## Usage

After installation, you can run the application using `tsx` followed by the script name, for example:

**From root**

```bash
npx tsx ./samples/typescript/index.ts --help
```

**From this folder**

```bash
npx tsx index.ts --help
```

### Commands

- **List TODOs**

  To list all TODO items, use:

  ```bash
  npx tsx index.ts list
  ```

- **Add a TODO**

  To add a new TODO item, use:

  ```bash
  npx tsx index.ts add "<title>" [status] [description]
  ```

  Status is optional and can be one of `NotStarted`, `InProgress`, or `Completed`. The default status is `NotStarted`.

- **Update a TODO**

  To update an existing TODO item's status, use:

  ```bash
  npx tsx index.ts update <id> <status>
  ```

- **Delete a TODO**

  To delete a TODO item, use:

  ```bash
  npx tsx index.ts delete <id>
  ```
