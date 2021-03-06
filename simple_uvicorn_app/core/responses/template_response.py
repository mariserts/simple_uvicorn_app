from .base import BaseResponse
from ..templates.template import Template


class TemplateResponse(BaseResponse):

    content_type = 'text/html'

    def __init__(self, template, context, status=None, headers=[]):
        self.template = template
        self.context = context
        self._status = status
        self._headers = headers
        self.response = self.get_response()

    @property
    def body(self):
        data = Template(self.template, self.context).render
        return str.encode(data)
