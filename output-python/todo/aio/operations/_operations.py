# coding=utf-8

from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, List, Optional, TYPE_CHECKING, Type, TypeVar, Union, cast, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ...operations._operations import (
    build_todo_items_attachments_create_attachment_request,
    build_todo_items_attachments_list_request,
    build_todo_items_create_request,
    build_todo_items_delete_request,
    build_todo_items_get_request,
    build_todo_items_list_request,
    build_todo_items_update_request,
    build_users_create_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore

if TYPE_CHECKING:
    from ... import _types
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]
_Unset: Any = object()


class UsersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~todo.aio.TodoClient`'s
        :attr:`users` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create(
        self, user: _models.User, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CreateResponse1:
        """create.

        :param user: Required.
        :type user: ~todo.models.User
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CreateResponse1. The CreateResponse1 is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse1
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self, user: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CreateResponse1:
        """create.

        :param user: Required.
        :type user: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CreateResponse1. The CreateResponse1 is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse1
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self, user: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CreateResponse1:
        """create.

        :param user: Required.
        :type user: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CreateResponse1. The CreateResponse1 is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse1
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def create(self, user: Union[_models.User, JSON, IO[bytes]], **kwargs: Any) -> _models.CreateResponse1:
        """create.

        :param user: Is one of the following types: User, JSON, IO[bytes] Required.
        :type user: ~todo.models.User or JSON or IO[bytes]
        :return: CreateResponse1. The CreateResponse1 is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse1
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            304: ResourceNotModifiedError,
            409: cast(
                Type[HttpResponseError],
                lambda response: ResourceExistsError(
                    response=response, model=_deserialize(_models.UserExistsResponse, response.json())
                ),
            ),
            422: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.InvalidUserResponse, response.json())
                ),
            ),
            400: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard4XXResponse, response.json())
                ),
            ),
            500: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard5XXResponse, response.json())
                ),
            ),
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CreateResponse1] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(user, (IOBase, bytes)):
            _content = user
        else:
            _content = json.dumps(user, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_users_create_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)  # type: ignore
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.CreateResponse1, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class TodoItemsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~todo.aio.TodoClient`'s
        :attr:`todo_items` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

        self.attachments = TodoItemsAttachmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    async def list(
        self, *, limit: Optional[int] = None, offset: Optional[int] = None, **kwargs: Any
    ) -> _models.TodoPage:
        """list.

        :keyword limit: The limit to the number of items. Default value is None.
        :paramtype limit: int
        :keyword offset: The offset to start paginating at. Default value is None.
        :paramtype offset: int
        :return: TodoPage. The TodoPage is compatible with MutableMapping
        :rtype: ~todo.models.TodoPage
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
            400: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard4XXResponse, response.json())
                ),
            ),
            500: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard5XXResponse, response.json())
                ),
            ),
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.TodoPage] = kwargs.pop("cls", None)

        _request = build_todo_items_list_request(
            limit=limit,
            offset=offset,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.TodoPage, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CreateResponse:
        """create.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CreateResponse. The CreateResponse is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        *,
        item: _models.TodoItem,
        content_type: str = "application/json",
        attachments: Optional[List["_types.TodoAttachment"]] = None,
        **kwargs: Any
    ) -> _models.CreateResponse:
        """create.

        :keyword item: Required.
        :paramtype item: ~todo.models.TodoItem
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword attachments: Default value is None.
        :paramtype attachments: list[~todo.models.TodoFileAttachment or ~todo.models.TodoUrlAttachment]
        :return: CreateResponse. The CreateResponse is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CreateResponse:
        """create.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CreateResponse. The CreateResponse is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def create(
        self,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        item: _models.TodoItem = _Unset,
        attachments: Optional[List["_types.TodoAttachment"]] = None,
        **kwargs: Any
    ) -> _models.CreateResponse:
        """create.

        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword item: Required.
        :paramtype item: ~todo.models.TodoItem
        :keyword attachments: Default value is None.
        :paramtype attachments: list[~todo.models.TodoFileAttachment or ~todo.models.TodoUrlAttachment]
        :return: CreateResponse. The CreateResponse is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
            422: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.InvalidTodoItem, response.json())
                ),
            ),
            400: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard4XXResponse, response.json())
                ),
            ),
            500: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard5XXResponse, response.json())
                ),
            ),
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[_models.CreateResponse] = kwargs.pop("cls", None)

        if body is _Unset:
            if item is _Unset:
                raise TypeError("missing required argument: item")
            body = {"attachments": attachments, "item": item}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_todo_items_create_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.CreateResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def get(self, id: int, **kwargs: Any) -> Optional[_models.GetResponse]:
        """get.

        :param id: Required.
        :type id: int
        :return: GetResponse or None. The GetResponse is compatible with MutableMapping
        :rtype: ~todo.models.GetResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Optional[_models.GetResponse]] = kwargs.pop("cls", None)

        _request = build_todo_items_get_request(
            id=id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200, 404]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.GetResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        id: int,
        patch: _models.TodoItemPatch,
        *,
        content_type: str = "application/merge-patch+json",
        **kwargs: Any
    ) -> _models.UpdateResponse:
        """update.

        :param id: Required.
        :type id: int
        :param patch: Required.
        :type patch: ~todo.models.TodoItemPatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: UpdateResponse. The UpdateResponse is compatible with MutableMapping
        :rtype: ~todo.models.UpdateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, id: int, patch: JSON, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.UpdateResponse:
        """update.

        :param id: Required.
        :type id: int
        :param patch: Required.
        :type patch: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: UpdateResponse. The UpdateResponse is compatible with MutableMapping
        :rtype: ~todo.models.UpdateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, id: int, patch: IO[bytes], *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.UpdateResponse:
        """update.

        :param id: Required.
        :type id: int
        :param patch: Required.
        :type patch: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: UpdateResponse. The UpdateResponse is compatible with MutableMapping
        :rtype: ~todo.models.UpdateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def update(
        self, id: int, patch: Union[_models.TodoItemPatch, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.UpdateResponse:
        """update.

        :param id: Required.
        :type id: int
        :param patch: Is one of the following types: TodoItemPatch, JSON, IO[bytes] Required.
        :type patch: ~todo.models.TodoItemPatch or JSON or IO[bytes]
        :return: UpdateResponse. The UpdateResponse is compatible with MutableMapping
        :rtype: ~todo.models.UpdateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[_models.UpdateResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/merge-patch+json"
        _content = None
        if isinstance(patch, (IOBase, bytes)):
            _content = patch
        else:
            _content = json.dumps(patch, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_todo_items_update_request(
            id=id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.UpdateResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def delete(self, id: int, **kwargs: Any) -> None:
        """delete.

        :param id: Required.
        :type id: int
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
            400: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard4XXResponse, response.json())
                ),
            ),
            500: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard5XXResponse, response.json())
                ),
            ),
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_todo_items_delete_request(
            id=id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore


class TodoItemsAttachmentsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~todo.aio.TodoClient`'s
        :attr:`attachments` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def list(self, item_id: int, **kwargs: Any) -> Optional[_models.PageTodoAttachment]:
        """list.

        :param item_id: Required.
        :type item_id: int
        :return: PageTodoAttachment or None. The PageTodoAttachment is compatible with MutableMapping
        :rtype: ~todo.models.PageTodoAttachment or None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
            400: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard4XXResponse, response.json())
                ),
            ),
            500: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard5XXResponse, response.json())
                ),
            ),
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Optional[_models.PageTodoAttachment]] = kwargs.pop("cls", None)

        _request = build_todo_items_attachments_list_request(
            item_id=item_id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200, 404]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.PageTodoAttachment, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_attachment(
        self,
        item_id: int,
        contents: _models.TodoFileAttachment,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """create_attachment.

        :param item_id: Required.
        :type item_id: int
        :param contents: Required.
        :type contents: ~todo.models.TodoFileAttachment
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create_attachment(
        self,
        item_id: int,
        contents: _models.TodoUrlAttachment,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """create_attachment.

        :param item_id: Required.
        :type item_id: int
        :param contents: Required.
        :type contents: ~todo.models.TodoUrlAttachment
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def create_attachment(self, item_id: int, contents: "_types.TodoAttachment", **kwargs: Any) -> None:
        """create_attachment.

        :param item_id: Required.
        :type item_id: int
        :param contents: Is either a TodoFileAttachment type or a TodoUrlAttachment type. Required.
        :type contents: ~todo.models.TodoFileAttachment or ~todo.models.TodoUrlAttachment
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
            400: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard4XXResponse, response.json())
                ),
            ),
            500: cast(
                Type[HttpResponseError],
                lambda response: HttpResponseError(
                    response=response, model=_deserialize(_models.Standard5XXResponse, response.json())
                ),
            ),
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(contents, _model_base.Model):
            _content = json.dumps(contents, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore
        elif isinstance(contents, _model_base.Model):
            _content = json.dumps(contents, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_todo_items_attachments_create_attachment_request(
            item_id=item_id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
