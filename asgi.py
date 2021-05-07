from simple_uvicorn_app.core.application import Application

import settings


app = Application(router=settings.Router)
