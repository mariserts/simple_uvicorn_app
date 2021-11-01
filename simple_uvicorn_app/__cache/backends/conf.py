from ...conf import settings as sua_settings


class Settings:

    @property
    def DEFAULT_TIMEOUT(self):
        return getattr(
            sua_settings,
            'DEFAULT_TIMEOUT',
            300
        )

    # Simple cache

    @property
    def SIMPLE_THRESHOLD(self):
        return getattr(
            sua_settings,
            'SIMPLE_THRESHOLD',
            500
        )

    # Redis cache

    @property
    def REDIS_HOST(self):
        return getattr(
            sua_settings,
            'REDIS_HOST',
            'localhost'
        )

    @property
    def REDIS_PORT(self):
        return getattr(
            sua_settings,
            'REDIS_PORT',
            6379
        )

    @property
    def REDIS_PASSWORD(self):
        return getattr(
            sua_settings,
            'REDIS_PORT',
            None
        )

    @property
    def REDIS_DB(self):
        return getattr(
            sua_settings,
            'REDIS_DB',
            0
        )

    @property
    def REDIS_KEY_PREFIX(self):
        return getattr(
            sua_settings,
            'REDIS_KEY_PREFIX',
            None
        )


settings = Settings()
