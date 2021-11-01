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
                return route

        return None   # TODO: Exception required if None

    def get_response(self, request):

        request_path = request.scope['path']
        request_method = request.scope['method'].lower()

        cache_backend = get_cache_backend()
        if cache_backend is not None:
            cached_value = cache_backend.get(request.url)
            if cached_value is not  None:
                return cached_value

        route = self.find_route(request)

        return getattr(
            route.viewset(),
            request_method
        )(request, **p_.groupdict()).response
