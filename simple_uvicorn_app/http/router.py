import re

from ..cache.utils import get_cache_backend
from ..views.viewsets import Viewset
from .conf import settings
from .responses import NotImplementedResponse, ServerErrorResponse


class BaseRoute:

    def __init__(self, regexp, viewset, cache=False):
        self.cache = False
        self.regexp = regexp
        self.viewset = viewset


class BaseRouter:

    routes = {}

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
        self.routes[route.regexp] = route

    def get_route_response(self, request):

        request_path = request.scope['path']
        request_method = request.scope['method'].lower()

        if request_method not in self.supported_http_methods:
            return self.server_error_response().response

        cache_backend = get_cache_backend()
        if cache_backend is not None:
            cached_value = cache_backend.get(request.url)
            if cached_value is not  None:
                return cached_value

        for regex, route in self.routes.items():

            r_ = re.compile(regex)
            p_ = r_.match(request_path)

            if p_ is not None:

                if hasattr(route.viewset, request_method) is False:
                    return self.not_implemented_response().response

                return getattr(
                    route.viewset(),
                    request_method
                )(request, **p_.groupdict()).response

        return self.server_error_response().response


class Route(BaseRoute):
    pass


class Router(BaseRouter):
    pass
