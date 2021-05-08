__all__ = [
    'Request'
]


class BaseRequest:
    def __init__(self, scope, session=None):
        self._session = session
        self._scope = scope

    @property
    def session(self):
        return self._session

    @property
    def scope(self):
        return self._scope


class Request(BaseRequest):
    pass
