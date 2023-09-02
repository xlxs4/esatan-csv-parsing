from pathlib import Path

from pyprojroot import here

_PATHS = {"config": "src/config.toml"}


def get_path(name: str, relative: bool) -> Path:
    return here(_PATHS[name]) if not relative else _PATHS[name]
