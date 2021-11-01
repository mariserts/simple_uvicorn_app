class Settings:

    # CACHE

    CACHE_BACKEND = (
        'simple_uvicorn_app.cache.backends.simple.SimpleCacheBackend')

    DEFAULT_TIMEOUT = 300

    # TEMPLATES

    JINJA2_EXTENSIONS = []
    TEMPLATE_DIRS = ['templates']

    @property
    def SUPPORTED_HTTP_METHODS(self):
        return [
            'connect',
            'delete',
            'get',
            'head',
            'options',
            'patch',
            'post',
            'put',
            'trace',
        ]

    @property
    def SUA_CACHE_KEY_NAME(self):
        return 'CACHE'


settings =  Settings()


class ProxySettings:
    def __getattr__(self, name):
        return getattr(settings, name, None)
