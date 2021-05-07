from simple_uvicorn_app.conf import settings as uv_settings


class Settings:

    @property
    def SUPPORTED_HTTP_METHODS(self):
        return getattr(
            uv_settings,
            'SUPPORTED_HTTP_METHODS',
            []
        )


settings =  Settings()
