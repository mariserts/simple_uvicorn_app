from simple_uvicorn_app.core.responses.template_response import TemplateResponse
from simple_uvicorn_app.core.viewsets.views import Viewset


class HomeView(Viewset):

    def get(self, request, language=None):
        print('Home with no caching')
        return TemplateResponse(template='project/base.html', context={})


class HomeWithLanguageView(Viewset):

    def get(self, request, language=None):
        print('Home with caching')
        return TemplateResponse(template='project/base.html', context={})
