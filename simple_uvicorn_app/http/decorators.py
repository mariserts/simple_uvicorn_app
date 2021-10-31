from functools import wraps

from ..conf import settings as sua_settings
from ..cache.conf import settings as cache_settings
from ..cache.utils import get_cache_backend


def cached_response(timeout=cache_settings.DEFAULT_TIMEOUT):

    def wrapper(method):

        @wraps(method)
        def wrapped(self, request, *method_args, **method_kwargs):

            response = method(
                self,
                request,
                *method_args,
                **method_kwargs
            )

            cache_backend = get_cache_backend()
            if cache_backend is not None:
                cached_value = cache_backend.get(request.url)
                if cached_value is None:
                    cache_backend.set(
                        request.url,
                        response.response,
                        timeout=timeout
                    )

            return response

        return wrapped

    return wrapper
