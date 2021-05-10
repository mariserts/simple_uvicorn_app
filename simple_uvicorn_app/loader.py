import importlib


def load_module_from_string(module_as_string):
    return importlib.import_module(module_as_string)


def load_module_class_from_string(module_class_as_string):
    parts = module_class_as_string.split('.')
    cls = parts.pop()
    module = load_module_from_string('.'.join(parts))
    return getattr(module, cls)
