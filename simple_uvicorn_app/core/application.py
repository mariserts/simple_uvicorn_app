from ..conf import settings


class BaseApplication:

    def __init__(self, router=None):
        setattr(settings, 'Router', router)

    async def __call__(self, scope, receive, send):

        response = settings.Router.get_route_response(scope)

        assert scope['type'] == 'http'

        await send({
            'type': 'http.response.start',
            'status': response['status'],
            'headers': response['headers'],
        })

        await send({
            'type': 'http.response.body',
            'body': response['body'],
        })


class Application(BaseApplication):
    pass
