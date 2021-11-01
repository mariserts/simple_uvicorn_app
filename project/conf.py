import os

from simple_uvicorn_app.core.routing.route import Route

from .views import HomeView, HomeWithLanguageView


APP_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT_DIR_NAME = os.path.split(APP_DIR)[1]


TEMPLATE_DIRS = [
    f'{PROJECT_ROOT_DIR_NAME}/templates'
]


ROUTES = [
    Route(r'^\/(?P<language>[a-z]*)\/$', HomeWithLanguageView),
    Route(r'^\/?$', HomeView)
]
