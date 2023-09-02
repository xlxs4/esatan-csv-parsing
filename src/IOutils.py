from tomllib import load

from config_model import Config


def _read_toml(filename):
    with open(filename, mode="rb") as fp:
        config = load(fp)
    return config


def read_config(filename):
    conf = _read_toml(filename)
    return Config.model_validate(conf)
