from cachelib.simple import SimpleCache

from .conf import settings


class SimpleCacheBackend(SimpleCache):

    def __init__(self):

        threshold = settings.SIMPLE_THRESHOLD
        default_timeout = settings.DEFAULT_TIMEOUT

        super().__init__(
            threshold=threshold,
            default_timeout=default_timeout
        )
