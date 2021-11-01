from ..conf import GlobalSettings


class Settings(GlobalSettings):

    JINJA2_EXTENSIONS = []
    TEMPLATE_DIRS = []


settings = GlobalSettings()
