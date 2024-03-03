// Licensed under the MIT license.

import {
  UsersCreateParameters,
  UsersValidateParameters,
  UsersLoginParameters,
  UsersLogoutParameters,
  UsersForgotPasswordParameters,
  UsersResetPasswordParameters,
  TodoItemsListParameters,
  TodoItemsCreateJsonParameters,
  TodoItemsCreateFormParameters,
  TodoItemsGetParameters,
  TodoItemsUpdateParameters,
  TodoItemsDeleteParameters,
  TodoItemsAttachmentsListParameters,
  TodoItemsAttachmentsCreateUrlAttachmentParameters,
  TodoItemsAttachmentsCreateFileAttachmentParameters,
} from "./parameters";
import {
  UsersCreate200Response,
  UsersCreate400Response,
  UsersCreate409Response,
  UsersCreate422Response,
  UsersCreate500Response,
  UsersValidate204Response,
  UsersValidate400Response,
  UsersValidate422Response,
  UsersValidate500Response,
  UsersLogin204Response,
  UsersLogin400Response,
  UsersLogin401Response,
  UsersLogin500Response,
  UsersLogout200Response,
  UsersForgotPassword204Response,
  UsersForgotPassword400Response,
  UsersForgotPassword404Response,
  UsersForgotPassword500Response,
  UsersResetPassword204Response,
  UsersResetPassword400Response,
  UsersResetPassword404Response,
  UsersResetPassword500Response,
  TodoItemsList200Response,
  TodoItemsList400Response,
  TodoItemsList500Response,
  TodoItemsCreateJson200Response,
  TodoItemsCreateJson400Response,
  TodoItemsCreateJson422Response,
  TodoItemsCreateJson500Response,
  TodoItemsCreateForm200Response,
  TodoItemsCreateForm400Response,
  TodoItemsCreateForm422Response,
  TodoItemsCreateForm500Response,
  TodoItemsGet200Response,
  TodoItemsGet404Response,
  TodoItemsUpdate200Response,
  TodoItemsDeleteOperation204Response,
  TodoItemsDeleteOperation400Response,
  TodoItemsDeleteOperation404Response,
  TodoItemsDeleteOperation500Response,
  TodoItemsAttachmentsList200Response,
  TodoItemsAttachmentsList400Response,
  TodoItemsAttachmentsList404Response,
  TodoItemsAttachmentsList500Response,
  TodoItemsAttachmentsCreateUrlAttachment204Response,
  TodoItemsAttachmentsCreateUrlAttachment400Response,
  TodoItemsAttachmentsCreateUrlAttachment404Response,
  TodoItemsAttachmentsCreateUrlAttachment500Response,
  TodoItemsAttachmentsCreateFileAttachment204Response,
  TodoItemsAttachmentsCreateFileAttachment400Response,
  TodoItemsAttachmentsCreateFileAttachment404Response,
  TodoItemsAttachmentsCreateFileAttachment500Response,
} from "./responses";
import { Client, StreamableMethod } from "@typespec/ts-http-runtime";

export interface UsersCreate {
  post(
    options: UsersCreateParameters,
  ): StreamableMethod<
    | UsersCreate200Response
    | UsersCreate400Response
    | UsersCreate409Response
    | UsersCreate422Response
    | UsersCreate500Response
  >;
}

export interface UsersValidate {
  get(
    options: UsersValidateParameters,
  ): StreamableMethod<
    | UsersValidate204Response
    | UsersValidate400Response
    | UsersValidate422Response
    | UsersValidate500Response
  >;
}

export interface UsersLogin {
  post(
    options?: UsersLoginParameters,
  ): StreamableMethod<
    | UsersLogin204Response
    | UsersLogin400Response
    | UsersLogin401Response
    | UsersLogin500Response
  >;
}

export interface UsersLogout {
  get(
    options?: UsersLogoutParameters,
  ): StreamableMethod<UsersLogout200Response>;
}

export interface UsersForgotPassword {
  /** Sends a reset token to the user's email address */
  post(
    options?: UsersForgotPasswordParameters,
  ): StreamableMethod<
    | UsersForgotPassword204Response
    | UsersForgotPassword400Response
    | UsersForgotPassword404Response
    | UsersForgotPassword500Response
  >;
}

export interface UsersResetPassword {
  get(
    options: UsersResetPasswordParameters,
  ): StreamableMethod<
    | UsersResetPassword204Response
    | UsersResetPassword400Response
    | UsersResetPassword404Response
    | UsersResetPassword500Response
  >;
}

export interface TodoItemsList {
  get(
    options?: TodoItemsListParameters,
  ): StreamableMethod<
    | TodoItemsList200Response
    | TodoItemsList400Response
    | TodoItemsList500Response
  >;
  post(
    options: TodoItemsCreateJsonParameters,
  ): StreamableMethod<
    | TodoItemsCreateJson200Response
    | TodoItemsCreateJson400Response
    | TodoItemsCreateJson422Response
    | TodoItemsCreateJson500Response
  >;
  post(
    options: TodoItemsCreateFormParameters,
  ): StreamableMethod<
    | TodoItemsCreateForm200Response
    | TodoItemsCreateForm400Response
    | TodoItemsCreateForm422Response
    | TodoItemsCreateForm500Response
  >;
}

export interface TodoItemsGet {
  get(
    options?: TodoItemsGetParameters,
  ): StreamableMethod<TodoItemsGet200Response | TodoItemsGet404Response>;
  patch(
    options: TodoItemsUpdateParameters,
  ): StreamableMethod<TodoItemsUpdate200Response>;
  delete(
    options?: TodoItemsDeleteParameters,
  ): StreamableMethod<
    | TodoItemsDeleteOperation204Response
    | TodoItemsDeleteOperation400Response
    | TodoItemsDeleteOperation404Response
    | TodoItemsDeleteOperation500Response
  >;
}

export interface TodoItemsAttachmentsList {
  get(
    options?: TodoItemsAttachmentsListParameters,
  ): StreamableMethod<
    | TodoItemsAttachmentsList200Response
    | TodoItemsAttachmentsList400Response
    | TodoItemsAttachmentsList404Response
    | TodoItemsAttachmentsList500Response
  >;
  post(
    options: TodoItemsAttachmentsCreateUrlAttachmentParameters,
  ): StreamableMethod<
    | TodoItemsAttachmentsCreateUrlAttachment204Response
    | TodoItemsAttachmentsCreateUrlAttachment400Response
    | TodoItemsAttachmentsCreateUrlAttachment404Response
    | TodoItemsAttachmentsCreateUrlAttachment500Response
  >;
  post(
    options: TodoItemsAttachmentsCreateFileAttachmentParameters,
  ): StreamableMethod<
    | TodoItemsAttachmentsCreateFileAttachment204Response
    | TodoItemsAttachmentsCreateFileAttachment400Response
    | TodoItemsAttachmentsCreateFileAttachment404Response
    | TodoItemsAttachmentsCreateFileAttachment500Response
  >;
}

export interface Routes {
  /** Resource for '/users' has methods for the following verbs: post */
  (path: "/users"): UsersCreate;
  /** Resource for '/validate' has methods for the following verbs: get */
  (path: "/validate"): UsersValidate;
  /** Resource for '/login' has methods for the following verbs: post */
  (path: "/login"): UsersLogin;
  /** Resource for '/logout' has methods for the following verbs: get */
  (path: "/logout"): UsersLogout;
  /** Resource for '/forgot-password' has methods for the following verbs: post */
  (path: "/forgot-password"): UsersForgotPassword;
  /** Resource for '/reset-password' has methods for the following verbs: get */
  (path: "/reset-password"): UsersResetPassword;
  /** Resource for '/items' has methods for the following verbs: get, post */
  (path: "/items"): TodoItemsList;
  /** Resource for '/items/\{id\}' has methods for the following verbs: get, patch, delete */
  (path: "/items/{id}", id: number): TodoItemsGet;
  /** Resource for '/items/\{itemId\}/attachments' has methods for the following verbs: get, post */
  (
    path: "/items/{itemId}/attachments",
    itemId: number,
  ): TodoItemsAttachmentsList;
}

export type TodoApplicationClient = Client & {
  path: Routes;
};
