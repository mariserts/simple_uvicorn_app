from functools import wraps

from ..conf import settings as sua_settings
from ..cache.conf import settings as cache_settings


def cached_response(timeout=cache_settings.DEFAULT_TIMEOUT):
    def wrapper(method):
        @wraps(method)
        def wrapped(self, request, *method_args, **method_kwargs):

            cache = getattr(
                sua_settings,
                sua_settings.SUA_CACHE_KEY_NAME,
                None
            )

            if cache is not None:

                cache_key = request.url
                cached_value = cache.get(cache_key)

                if cached_value is None:

                    response = method(
                        self,
                        request,
                        *method_args,
                        **method_kwargs
                    )

                    cached_value = response
                    cache.set(cache_key, cached_value, timeout=timeout)

            return cached_value

        return wrapped
    return wrapper
