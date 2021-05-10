import sys

from .conf import settings
from .loader import load_module_class_from_string
from .http.router import Router


class BaseApplication:

    def __init__(self, extra_settings):
        self.router = Router()
        self.extra_settings = extra_settings
        self.load_application()

    async def __call__(self, scope, receive, send):

        response = self.router.get_route_response(scope)

        assert scope['type'] == 'http'

        await send({
            'type': 'http.response.start',
            'status': response['status'],
            'headers': response['headers'],
        })

        await send({
            'type': 'http.response.body',
            'body': response['body'],
        })

    @property
    def EXTRA_SETTINGS_APP_ROOT(self):
        return getattr(self.extra_settings, 'APP_ROOT', None)

    @property
    def EXTRA_SETTINGS_PROJECT_ROOT_DIR_name(self):
        return getattr(self.extra_settings, 'PROJECT_ROOT_DIR_NAME', None)

    @property
    def EXTRA_SETTINGS_ROUTES(self):
        return getattr(self.extra_settings, 'ROUTES', [])

    @property
    def EXTRA_SETTINGS_TEMPLATE_DIRS(self):
        return getattr(self.extra_settings, 'TEMPLATE_DIRS', [])

    @property
    def EXTRA_JINJA2_EXTENSIONS(self):
        return getattr(self.extra_settings, 'EXTRA_JINJA2_EXTENSIONS', [])

    def load_application(self):

        # Add root app

        root = f'{self.EXTRA_SETTINGS_APP_ROOT}'
        root += '.'
        root += f'{self.EXTRA_SETTINGS_PROJECT_ROOT_DIR_name}'

        sys.path.append(root)

        # Add routes
        for route in self.EXTRA_SETTINGS_ROUTES:
            self.router.add_route(route)

        # Extend templates
        settings.TEMPLATE_DIRS += self.EXTRA_SETTINGS_TEMPLATE_DIRS

        # Extend jinja2 extensions
        settings.JINJA2_EXTENSIONS += self.EXTRA_JINJA2_EXTENSIONS

        # Set cache
        setattr(
            settings,
            settings.SUA_CACHE_KEY_NAME,
            load_module_class_from_string(settings.CACHE_BACKEND)()
        )


class Application(BaseApplication):
    pass
