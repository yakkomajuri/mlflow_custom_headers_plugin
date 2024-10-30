import os
from mlflow.tracking.request_header.abstract_request_header_provider import (
    RequestHeaderProvider,
)


class CustomRequestHeaderProvider(RequestHeaderProvider):
    """RequestHeaderProvider provided through plugin system"""

    def in_context(self):
        return True

    def request_headers(self):
        request_headers = dict()
        custom_headers_str = os.getenv("MLFLOW_CUSTOM_HEADERS", None)

        if not custom_headers_str:
            return request_headers

        for header_pair in custom_headers_str.split(","):
            header_name, header_value = header_pair.split(":")
            request_headers[header_name] = header_value

        return request_headers
