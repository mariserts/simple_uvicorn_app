from simple_uvicorn_app.conf import settings as uv_settings
from simple_uvicorn_app.core.cache.backends.simple_cache import cache
from simple_uvicorn_app.core.http.router import Router as _Router
from simple_uvicorn_app.core.http.router import Route

from views import HomeView


uv_settings.cache = cache


Router = _Router()

Router.add_route(Route(r'^\/(?P<language>[a-z]*)\/$', HomeView))
Router.add_route(Route(r'', HomeView))
