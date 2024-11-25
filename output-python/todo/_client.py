# coding=utf-8


from copy import deepcopy
from typing import Any, Union
from typing_extensions import Self

from corehttp.credentials import ServiceKeyCredential
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import TodoClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import TodoItemsOperations, UsersOperations


class TodoClient:  # pylint: disable=client-accepts-api-version-keyword
    """TodoClient.

    :ivar users: UsersOperations operations
    :vartype users: todo.operations.UsersOperations
    :ivar todo_items: TodoItemsOperations operations
    :vartype todo_items: todo.operations.TodoItemsOperations
    :param endpoint: Service host. Required.
    :type endpoint: str
    :param credential: Credential used to authenticate requests to the service. Is either a
     ServiceKeyCredential type or a ServiceKeyCredential type. Required.
    :type credential: ~corehttp.credentials.ServiceKeyCredential or
     ~corehttp.credentials.ServiceKeyCredential
    """

    def __init__(self, endpoint: str, credential: ServiceKeyCredential, **kwargs: Any) -> None:
        _endpoint = "{endpoint}"
        self._config = TodoClientConfiguration(endpoint=endpoint, credential=credential, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.logging_policy,
            ]
        self._client: PipelineClient = PipelineClient(endpoint=_endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.users = UsersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.todo_items = TodoItemsOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from corehttp.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~corehttp.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~corehttp.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
