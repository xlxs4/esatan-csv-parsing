from pyprojroot import here

_PATHS = {"config": "src/config.toml"}


def get_path(name, relative):
    return here(_PATHS[name]) if not relative else _PATHS[name]
