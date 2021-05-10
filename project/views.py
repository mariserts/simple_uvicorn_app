from simple_uvicorn_app.http.decorators import cached_response
from simple_uvicorn_app.http.responses import TemplateResponse
from simple_uvicorn_app.views import viewsets


class HomeView(viewsets.Viewset):

    @cached_response(10)
    def get(self, request, language=None):
        return TemplateResponse(template='project/base.html', context={})
