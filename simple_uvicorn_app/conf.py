class Settings:

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
    def TEMPLATE_DIRS(self):
        return ['templates']


settings =  Settings()
