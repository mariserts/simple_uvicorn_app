from simple_uvicorn_app.http.decorators import cached_response
from simple_uvicorn_app.http.responses import TemplateResponse
from simple_uvicorn_app.views import viewsets


class HomeView(viewsets.Viewset):

    def get(self, request, language=None):
        print('Home with no caching')
        return TemplateResponse(template='project/base.html', context={})


class HomeWithLanguageView(viewsets.Viewset):

    @cached_response(2)
    def get(self, request, language=None):
        print('Home with caching')
        return TemplateResponse(template='project/base.html', context={})
