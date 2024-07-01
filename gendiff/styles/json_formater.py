import json


def json_formater(diff: dict):
    return json.dumps(diff, indent=2)
