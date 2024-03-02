# TypeSpec Todo

A todo application written in using TypeSpec.

The server is implemented in as much of an API-first way as possible. To start the server, run:

```
> npm install
> npm run build
> npm run start
```

Interesting features:

- TypeSpec, generating both JSON Schema and OpenAPI3.
- Docs are exposed under the `/docs` endpoint.
- TypeScript types are generated from JSON Schema using `json-schema-to-typescript`.
- Routes are attached and requests/responses are validated based on the OpenAPI using `fastify-openapi-glue`.

## Prerequisites

1. Install [node](https://nodejs.org).
2. For Python codegen, install [Python](https://python.org) and [pip](https://pip.pypa.io/en/stable/installation/).
