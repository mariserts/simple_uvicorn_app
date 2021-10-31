import uuid


class BaseSession:

    def __init__(self, scope):
        self._scope = scope
        self.id = uuid.uuid4()


class Session(BaseSession):
    pass
