import re

from ..responses.error_response import ServerErrorResponse


class BaseRoute:

    def __init__(self, regexp, viewset, cache=False, timeout=0):
        self.cache = False
        self.regexp = regexp
        self.viewset = viewset


class BaseRouter:

    routes = {}

    def __init__(self):
        pass

    def add_route(self, route):
        self.routes[route.regexp] = route

    def find_route(self, request):

        request_path = request.scope['path']

        for pattern, route in self.routes.items():
            r_ = re.compile(pattern)
            p_ = r_.match(request_path)
            if p_ is not None:
                return (route, p_)

        raise KeyError(f'Route for "{request_path}" is not found')

    def get_response(self, request):

        request_path = request.scope['path']
        request_method = request.scope['method'].lower()

        try:
            route, kwargs = self.find_route(request)
        except KeyError:
            return ServerErrorResponse()

        return getattr(
            route.viewset(),
            request_method
        )(request, **kwargs.groupdict()).response
