import re

from ..views.viewsets import Viewset
from .conf import settings
from .responses import NotImplementedResponse, ServerErrorResponse
from .requests import Request
from .sessions import Session


__all__ = [
    'BaseRouter',
    'Route',
    'Router',
]


class Route:
    def __init__(self, regexp, viewset):
        self.regexp = regexp
        self.viewset = viewset


class BaseRouter:

    routes = []

    def __init__(self):
        pass

    @property
    def server_error_response(self):
        return ServerErrorResponse

    @property
    def not_implemented_response(self):
        return NotImplementedResponse

    @property
    def supported_http_methods(self):
        return settings.SUPPORTED_HTTP_METHODS

    def add_route(self, route):
        self.routes.append(route)

    def get_route_response(self, scope):

        request = Request(
            scope,
            session=Session(scope)
        )

        request_path = request.scope['path']
        request_method = request.scope['method'].lower()

        if request_method not in self.supported_http_methods:
            return self.server_error_response().response

        for route in self.routes:

            r_ = re.compile(route.regexp)
            p_ = r_.match(request_path)

            if p_ is not None:

                if hasattr(route.viewset, request_method) is False:
                    return self.not_implemented_response()

                return getattr(
                    route.viewset(),
                    request_method
                )(request, **p_.groupdict()).response

        return self.server_error_response().response


class Router(BaseRouter):
    pass
