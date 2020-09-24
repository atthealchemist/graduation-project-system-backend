import random
import re
import string
from base64 import b64encode
from datetime import datetime
from hashlib import md5, sha256, pbkdf2_hmac
from pathlib import Path
from uuid import UUID

import yaml
from jwcrypto.jwk import JWK
from transliterate import translit


def extract_entity(query_set, exclude_fields=None):

    def extract_from_orm_dict(entity):
        item = list(entity.values())[0]
        first_key = list(item.keys())[0]
        entity_raw = item.get(first_key)
        return entity_raw

    def convert_types(value):
        if type(value) == UUID:
            value = value.hex
        if type(value) == datetime:
            value = str(value)
        return value

    def convert_entity(entity):
        entity_raw = extract_from_orm_dict(entity)
        entity_converted = {k: convert_types(v) for k, v in entity_raw.items()}
        if exclude_fields:
            entity_converted = {k: convert_types(v) for k, v in entity_raw.items() if k not in exclude_fields}
        return entity_converted

    result = []
    if type(query_set) == list:
        for entry in query_set:
            result.append(convert_entity(entry))
    else:
        result.append(convert_entity(query_set))

    return result if len(result) > 1 else result[0]


def generate_slug(name):
    cleaned = re.sub(r"[^A-Za-zА-Яa-я0-9ё]+", '_', translit(name, reversed=True))
    return cleaned.lower().strip('_')


def random_string(length):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
                   for _ in range(length))


def generate_jwt_token():
    key = JWK(generate='oct', size=512)
    return key.export(as_dict=True).get('k')


def encrypt_password(content, salt=random_string(64)):
    hashed = pbkdf2_hmac(
        hash_name='sha256',
        password=''.join(reversed(content)).encode(),
        salt=salt.encode(),
        iterations=10000
    ).hex()
    return hashed, salt


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
