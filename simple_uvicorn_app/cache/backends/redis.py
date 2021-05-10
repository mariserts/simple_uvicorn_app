from cachelib.redis import RedisCache

from .conf import settings


class RedisCacheBackend(RedisCache):

    def __init__(self):

        host = settings.REDIS_HOST
        port = settings.REDIS_PORT
        password = settings.REDIS_PASSWORD
        db = settings.REDIS_DB
        key_prefix = settings.REDIS_KEY_PREFIX
        default_timeout = settings.REDIS_DEFAULT_TIMEOUT

        super().__init__(
            host=host,
            port=port,
            password=password,
            db=db,
            default_timeout=default_timeout,
            key_prefix=key_prefix,
            **{}
        )
