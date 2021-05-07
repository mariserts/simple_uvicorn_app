from simple_uvicorn_app.core.application import Application

from . import settings


app = Application(router=settings.Router)
