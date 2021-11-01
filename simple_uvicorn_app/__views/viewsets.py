from ..http.responses import NotImplementedResponse

from .conf import settings


class BaseViewset:

    def __getattr__(self, name):
        if name in settings.SUPPORTED_HTTP_METHODS:
            return NotImplementedResponse()


class Viewset(BaseViewset):
    pass
