from functools import wraps


def cached_class_method(cache_key=None):
    def wrapper(method):
        @wraps(method)
        def wrapped(self, request, *method_args, **method_kwargs):
            print(self)
            print(request)
            print(method_args)
            print(method_kwargs)
            print(cache_key)
            return method(self, request, *method_args, **method_kwargs)
        return wrapped
    return wrapper
