import requests

from simple_uvicorn_app.conf import settings as uv_settings
from simple_uvicorn_app.core.http.responses import TemplateResponse
from simple_uvicorn_app.core.views import viewsets

class HomeView(viewsets.Viewset):
    def get(self, request, language=None):

        url = 'https://www.mygov.ie'

        cache_key = f'{url}'

        data = uv_settings.cache.get(cache_key)
        if data == uv_settings.cache.NOT_SET_VALUE:
            data = requests.get(url).text
            uv_settings.cache.set(cache_key, data, 5)

        return TemplateResponse(template='base.html', context={})
