from ...conf import settings as uv_settings


class Settings:

    @property
    def TEMPLATE_DIRS(self):
        return getattr(uv_settings, 'TEMPLATE_DIRS', ['templates'])


settings = Settings()
