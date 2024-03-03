// Licensed under the MIT license.

import { HttpResponse } from "@typespec/ts-http-runtime";
import {
  UserCreatedResponseOutput,
  ApiErrorOutput,
  UserExistsResponseOutput,
  InvalidUserResponseOutput,
  TodoPageOutput,
  TodoItemOutput,
  TodoAttachmentOutput,
} from "./outputModels";

/** The request has succeeded. */
export interface UsersCreate200Response extends HttpResponse {
  status: "200";
  body: UserCreatedResponseOutput;
}

/** Client error */
export interface UsersCreate400Response extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** The request conflicts with the current state of the server. */
export interface UsersCreate409Response extends HttpResponse {
  status: "409";
  body: UserExistsResponseOutput;
}

/** Client error */
export interface UsersCreate422Response extends HttpResponse {
  status: "422";
  body: InvalidUserResponseOutput;
}

/** Server error */
export interface UsersCreate500Response extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}

/** There is no content to send for this request, but the headers may be useful. */
export interface UsersValidate204Response extends HttpResponse {
  status: "204";
}

/** Client error */
export interface UsersValidate400Response extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** Client error */
export interface UsersValidate422Response extends HttpResponse {
  status: "422";
  body: InvalidUserResponseOutput;
}

/** Server error */
export interface UsersValidate500Response extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}

/** There is no content to send for this request, but the headers may be useful. */
export interface UsersLogin204Response extends HttpResponse {
  status: "204";
}

/** Client error */
export interface UsersLogin400Response extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** Access is unauthorized. */
export interface UsersLogin401Response extends HttpResponse {
  status: "401";
}

/** Server error */
export interface UsersLogin500Response extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}

/** The request has succeeded. */
export interface UsersLogout200Response extends HttpResponse {
  status: "200";
}

/** There is no content to send for this request, but the headers may be useful. */
export interface UsersForgotPassword204Response extends HttpResponse {
  status: "204";
}

/** Client error */
export interface UsersForgotPassword400Response extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** The server cannot find the requested resource. */
export interface UsersForgotPassword404Response extends HttpResponse {
  status: "404";
}

/** Server error */
export interface UsersForgotPassword500Response extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}

/** There is no content to send for this request, but the headers may be useful. */
export interface UsersResetPassword204Response extends HttpResponse {
  status: "204";
}

/** Client error */
export interface UsersResetPassword400Response extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** The server cannot find the requested resource. */
export interface UsersResetPassword404Response extends HttpResponse {
  status: "404";
}

/** Server error */
export interface UsersResetPassword500Response extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}

/** The request has succeeded. */
export interface TodoItemsList200Response extends HttpResponse {
  status: "200";
  body: TodoPageOutput;
}

/** Client error */
export interface TodoItemsList400Response extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** Server error */
export interface TodoItemsList500Response extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}

/** The request has succeeded. */
export interface TodoItemsCreateJson200Response extends HttpResponse {
  status: "200";
  body: TodoItemOutput;
}

/** Client error */
export interface TodoItemsCreateJson400Response extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** Client error */
export interface TodoItemsCreateJson422Response extends HttpResponse {
  status: "422";
  body: ApiErrorOutput;
}

/** Server error */
export interface TodoItemsCreateJson500Response extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}

/** The request has succeeded. */
export interface TodoItemsCreateForm200Response extends HttpResponse {
  status: "200";
  body: TodoItemOutput;
}

/** Client error */
export interface TodoItemsCreateForm400Response extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** Client error */
export interface TodoItemsCreateForm422Response extends HttpResponse {
  status: "422";
  body: ApiErrorOutput;
}

/** Server error */
export interface TodoItemsCreateForm500Response extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}

/** The request has succeeded. */
export interface TodoItemsGet200Response extends HttpResponse {
  status: "200";
  body: TodoItemOutput;
}

/** The server cannot find the requested resource. */
export interface TodoItemsGet404Response extends HttpResponse {
  status: "404";
}

/** The request has succeeded. */
export interface TodoItemsUpdate200Response extends HttpResponse {
  status: "200";
  body: TodoItemOutput;
}

/** There is no content to send for this request, but the headers may be useful. */
export interface TodoItemsDeleteOperation204Response extends HttpResponse {
  status: "204";
}

/** Client error */
export interface TodoItemsDeleteOperation400Response extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** The server cannot find the requested resource. */
export interface TodoItemsDeleteOperation404Response extends HttpResponse {
  status: "404";
}

/** Server error */
export interface TodoItemsDeleteOperation500Response extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}

/** The request has succeeded. */
export interface TodoItemsAttachmentsList200Response extends HttpResponse {
  status: "200";
  body: TodoAttachmentOutput[];
}

/** Client error */
export interface TodoItemsAttachmentsList400Response extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** The server cannot find the requested resource. */
export interface TodoItemsAttachmentsList404Response extends HttpResponse {
  status: "404";
}

/** Server error */
export interface TodoItemsAttachmentsList500Response extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}

/** There is no content to send for this request, but the headers may be useful. */
export interface TodoItemsAttachmentsCreateUrlAttachment204Response
  extends HttpResponse {
  status: "204";
}

/** Client error */
export interface TodoItemsAttachmentsCreateUrlAttachment400Response
  extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** The server cannot find the requested resource. */
export interface TodoItemsAttachmentsCreateUrlAttachment404Response
  extends HttpResponse {
  status: "404";
}

/** Server error */
export interface TodoItemsAttachmentsCreateUrlAttachment500Response
  extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}

/** There is no content to send for this request, but the headers may be useful. */
export interface TodoItemsAttachmentsCreateFileAttachment204Response
  extends HttpResponse {
  status: "204";
}

/** Client error */
export interface TodoItemsAttachmentsCreateFileAttachment400Response
  extends HttpResponse {
  status: "400";
  body: ApiErrorOutput;
}

/** The server cannot find the requested resource. */
export interface TodoItemsAttachmentsCreateFileAttachment404Response
  extends HttpResponse {
  status: "404";
}

/** Server error */
export interface TodoItemsAttachmentsCreateFileAttachment500Response
  extends HttpResponse {
  status: "500";
  body: ApiErrorOutput;
}
