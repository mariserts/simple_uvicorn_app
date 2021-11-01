from simple_uvicorn_app.core.applications.application import Application

from project import conf


app = Application(extra_settings=conf)
