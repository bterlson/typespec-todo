import Fastify from "fastify";
import fastifyMultipart from "@fastify/multipart";
import fastifyOpenapiGlue from "fastify-openapi-glue";
import fastifySwagger from "@fastify/swagger";
import fastifyReference from "@scalar/fastify-api-reference";

import { Service } from "./service.js";
const localFile = (fileName: string) =>
  new URL(fileName, import.meta.url).pathname;

const serviceHandlers = new Service();
const pluginOptions = {
  specification: localFile("../tsp-output/@typespec/openapi3/openapi.yaml"),
  serviceHandlers,
};

const fastify = Fastify({
  logger: true,
});
fastify.register(fastifyMultipart, {
  attachFieldsToBody: true
});
fastify.register(fastifyOpenapiGlue, pluginOptions);
fastify.register(fastifySwagger, {
  mode: "static",
  specification: {
    path: "tsp-output/@typespec/openapi3/openapi.yaml",
    baseDir: "tsp-output/@typespec/openapi3",
  },
});
fastify.register(fastifyReference, { routePrefix: "/ref" });
fastify.addContentTypeParser(
  "application/merge-patch+json",
  { parseAs: "string" },
  function (req, body: string, done) {
    try {
      const json = JSON.parse(body);
      done(null, json);
    } catch (err: any) {
      err.statusCode = 400;
      done(err, undefined);
    }
  }
);

/**
 * Handle validation errors. Other types of errors are handled by the service.
 */
fastify.setErrorHandler((error, req, res) => {
  if (error.validation) {
    let code;
    // todo: clean this up!
    try {
      code = (req.routeOptions.schema.response as any)["422"].properties.code.enum[0];
    } catch (e: any) {
      code = error.code;
    }

    switch (code) {
      case "invalid-user":
        res.status(422).send({
          code,
          message: error.validationContext + error.validation[0].instancePath + " " + error.validation[0].message ?? "The user is invalid",
        });
        return;
    }

    res.status(422).send({
      code: code ?? "serialization-error",
      message: error.validationContext + error.validation[0].instancePath + " " + error.validation[0].message ?? "The object is invalid"
    })
    return;
  }

  res.status(500).send({
    code: "server-error",
    message: error.message
  })

  throw error;
});

try {
  await fastify.listen({ port: 3000 });
} catch (err) {
  fastify.log.error(err);
  process.exit(1);
}
