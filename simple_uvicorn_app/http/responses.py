from ..templates.template import Template


class BaseResponse:

    def __init__(self, body, status=None, headers=[]):
        self._body = body
        self._status = status
        self._headers = headers
        self.response = self._response

    def __repr__(self):
        return self.response

    @property
    def body(self):

        if isinstance(self._body, dict) is True:
            return str.encode(json.dumps(self._body))

        if isinstance(self._body, str) is True:
            return str.encode(self._body)

        return b''

    @property
    def status(self):
        if self._status is None:
            return 200
        return self._status

    @property
    def content_type(self):
        return 'text/plain'

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

    @property
    def _response(self):
        return {
            'status': self.status,
            'headers': self.headers,
            'body': self.body,
        }


class JsonResponse(BaseResponse):

    @property
    def content_type(self):
        return 'application/json'


class TemplateResponse(BaseResponse):

    def __init__(self, template, context, status=None, headers=[]):
        self.template = template
        self.context = context
        self._status = status
        self._headers = headers
        self.response = self._response

    @property
    def body(self):
        data = Template(self.template, self.context).render
        return str.encode(data)

    @property
    def content_type(self):
        return 'text/html'


class ServerErrorResponse(BaseResponse):

    def __init__(self):
        self._status = 500

    @property
    def body(self):
        return str.encode(f'{self._status} Server error')



class NotImplementedResponse(BaseResponse):

    def __init__(self):
        self._status = 501
        message = f'{self._status} Request method is not implemented'
        super(BaseResponse)(None, message, self._status, None)
