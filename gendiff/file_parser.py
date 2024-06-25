from pathlib import PurePath
import json
import yaml


def read_file(path: str) -> dict:
    extention = PurePath(path).suffix

    with open(path, mode='r', encoding='utf-8') as file:
        content = file.read()

    match extention:
        case '.json':
            return json.loads(content)
        case '.yaml' | '.yml':
            return yaml.full_load(content)
        case _:
            raise ValueError(f"{extention} format not suppoted")
