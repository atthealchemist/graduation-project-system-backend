from pathlib import Path

import yaml


def load_config(config_path='config.yml'):
    config_path = Path(config_path)
    config = config_path
    # we can't find config in program folder
    if not config_path.exists():
        print("Config file {} was not found!".format(config_path))
        config = False
    with open(config, 'r+') as yaml_config:
        yaml_contents = yaml_config.read()
        config = yaml.safe_load(yaml_contents)
    return config
