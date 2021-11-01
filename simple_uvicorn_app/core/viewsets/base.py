class BaseViewset:

    ALLOWED_HTTP_METHODS = [
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

    def __init__(self):
        pass

    def __getattr__(self, name):

        if name in self.ALLOWED_HTTP_METHODS:
            return None # Raise not implemented
