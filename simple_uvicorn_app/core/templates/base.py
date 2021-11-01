import jinja2

from ..conf import settings as _settings


class BaseTemplate:

    settings = _settings

    def __init__(self, name, context):
        self._name = name
        self.context = context

    @property
    def loader(self):
        return jinja2.FileSystemLoader(self.template_dirs)

    @property
    def name(self):
        return self._name

    @property
    def source(self):
        return self.template_environment.get_template(self.name)

    @property
    def template_environment(self):
        return jinja2.Environment(
            loader=self.loader,
            extensions=self.settings.JINJA2_EXTENSIONS,
        )

    @property
    def template_dirs(self):
        return self.settings.TEMPLATE_DIRS

    @property
    def render(self):
        return self.source.render(self.context)
