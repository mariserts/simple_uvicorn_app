from .base import BaseResponse


class JsonResponse(BaseResponse):
    content_type = 'application/json'
