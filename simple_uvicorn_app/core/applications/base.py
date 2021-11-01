import sys

from ..conf import settings
from ..utils.loader import load_module_class_from_string

from ..requests.request import Request
from ..routing.router import Router


class BaseApplication:

    def __init__(self, extra_settings):
        self.settings = settings
        self.router = Router()
        self.extra_settings = extra_settings
        self.load_application()

    async def __call__(self, scope, receive, send):

        request = Request(scope)

        response = self.router.get_response(request)

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
        return getattr(self.extra_settings, 'JINJA2_EXTENSIONS', [])

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
        self.settings.TEMPLATE_DIRS += self.EXTRA_SETTINGS_TEMPLATE_DIRS

        # Extend jinja2 extensions
        self.settings.JINJA2_EXTENSIONS += self.EXTRA_JINJA2_EXTENSIONS
