from .base import BaseResponse


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
