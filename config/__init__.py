import yaml


def get_config_from_file(file):
    with open(file) as f:
        data = yaml.safe_load(f)
    return Config(data)


class Config:
    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                value = Config(value)

            setattr(self, key, value)


config = get_config_from_file("config.yml")
