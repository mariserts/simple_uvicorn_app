import json


class BaseResponse:

    content_type = 'text/plain'

    def __init__(self, body, status=None, headers=[]):
        self._body = body
        self._status = status
        self._headers = headers

        self.response = self.get_response()

    def __repr__(self):
        return self.response

    @property
    def body(self):

        if isinstance(self._body, dict) is True:
            return str.encode(json.dumps(self._body))

        if isinstance(self._body, str) is True:
            return str.encode(self._body)

        if isinstance(self._body, list) is True:
            return str.encode(json.dumps(self._body))

        return b''  # Raise

    @property
    def status(self):
        if self._status is None:
            return 200
        return self._status

    @property
    def headers(self):

        if getattr(self, '_headers', None) is None:
            self._headers = []

        headers = [
            [b'content-type', str.encode(self.content_type)]
        ]

        for header in self._headers:
            pass

        return headers

    def get_response(self):
        return {
            'status': self.status,
            'headers': self.headers,
            'body': self.body,
        }
