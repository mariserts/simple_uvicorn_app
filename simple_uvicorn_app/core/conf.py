class Settings:

    JINJA2_EXTENSIONS = []
    TEMPLATE_DIRS = [
        'templates'
    ]
    SUPPORTED_HTTP_METHODS = [
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


settings = Settings()
