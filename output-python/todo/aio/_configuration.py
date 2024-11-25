# coding=utf-8


from typing import Any, Union

from corehttp.credentials import ServiceKeyCredential
from corehttp.runtime import policies

from .._version import VERSION


class TodoClientConfiguration:
    """Configuration for TodoClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Service host. Required.
    :type endpoint: str
    :param credential: Credential used to authenticate requests to the service. Is either a
     ServiceKeyCredential type or a ServiceKeyCredential type. Required.
    :type credential: ~corehttp.credentials.ServiceKeyCredential or
     ~corehttp.credentials.ServiceKeyCredential
    """

    def __init__(self, endpoint: str, credential: ServiceKeyCredential, **kwargs: Any) -> None:
        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.endpoint = endpoint
        self.credential = credential
        kwargs.setdefault("sdk_moniker", "todo/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _infer_policy(self, **kwargs):
        if isinstance(self.credential, ServiceKeyCredential):
            return policies.ServiceKeyCredentialPolicy(self.credential, "Authorization", prefix="Bearer", **kwargs)
        if isinstance(self.credential, ServiceKeyCredential):
            return policies.ServiceKeyCredentialPolicy(self.credential, "session-id", **kwargs)
        raise TypeError(f"Unsupported credential: {self.credential}")

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.AsyncRetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = self._infer_policy(**kwargs)
