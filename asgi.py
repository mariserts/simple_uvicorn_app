from simple_uvicorn_app.application import Application

from project import settings as project_settings


app = Application(extra_settings=project_settings)
