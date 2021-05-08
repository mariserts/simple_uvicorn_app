class Settings:

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


settings =  Settings()


class ProxySettings:
    def __getattr__(self, name):
        return getattr(settings, name, None)
