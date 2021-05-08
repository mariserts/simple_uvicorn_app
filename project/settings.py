import os

from simple_uvicorn_app.http.router import Route

from .views import HomeView


APP_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT_DIR_NAME = 'project'

TEMPLATE_DIRS = [
    'project/templates'
]

ROUTES = [
    Route(r'^\/(?P<language>[a-z]*)\/$', HomeView),
    Route(r'', HomeView)
]
