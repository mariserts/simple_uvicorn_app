class BaseRequest:
    def __init__(self, scope, session=None):
        self._session = session
        self._scope = scope
        self._url = None

    @property
    def session(self):
        return self._session

    @property
    def scope(self):
        return self._scope

    @property
    def url(self):

        if self._url is None:

            scope = self.scope

            scheme = scope['scheme']

            host = scope['headers'][0][1].decode('utf-8')

            path = scope['raw_path'].decode('utf-8')

            query_string = scope['query_string'].decode('utf-8')
            if query_string != '':
                query_string = f'?{query_string}'

            self._url = f'{scheme}://'
            self._url += f'{host}/'
            self._url += f'{path}'
            self._url += f'{query_string}'

        return self._url


class Request(BaseRequest):
    pass
