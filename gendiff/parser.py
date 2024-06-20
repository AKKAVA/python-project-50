import json
import yaml


def parse_file(path: str) -> dict:
    extention = path.split('.')[-1]
    with open(path, mode='r', encoding='utf-8') as file:
        content = file.read()

    match extention:
        case 'json':
            return json.loads(content)
        case 'yaml' | 'yml':
            return yaml.full_load(content)
        case _:
            raise ValueError(f"{extention} format not suppoted")
