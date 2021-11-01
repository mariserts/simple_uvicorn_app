from .conf import settings


def get_cache_backend():
    return getattr(
        settings,
        settings.SUA_CACHE_KEY_NAME,
        None
    )
