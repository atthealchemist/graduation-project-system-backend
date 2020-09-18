import random
import string
from base64 import b64encode
from datetime import datetime
from hashlib import md5, sha256, pbkdf2_hmac
from pathlib import Path

import yaml
from jwcrypto.jwk import JWK


def random_string(length):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
                   for _ in range(length))


def generate_jwt_token():
    key = JWK(generate='oct', size=512)
    return key.export(as_dict=True).get('k')


def encrypt_password(content, salt=random_string(64)):
    return pbkdf2_hmac(
        hash_name='sha256',
        password=''.join(reversed(content)).encode(),
        salt=salt.encode(),
        iterations=10000
    ).hex()


def encrypt_base64(content):
    return b64encode(content.encode()).decode()


def load_config(section=False, config_path='config.yml'):
    config_path = Path(config_path)
    config = config_path
    # we can't find config in program folder
    if not config_path.exists():
        print("Config file {} was not found!".format(config_path))
        config = False
    with open(config, 'r+') as yaml_config:
        yaml_contents = yaml_config.read()
        config = yaml.safe_load(yaml_contents)
    if section:
        config = config.get(section)
    return config
