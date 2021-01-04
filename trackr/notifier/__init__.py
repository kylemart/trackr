from pkgutil import walk_packages
from importlib import import_module


for (_, module, _) in walk_packages(path=__path__, prefix=f'{__name__}.'):
    import_module(module)
