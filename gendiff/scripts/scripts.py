import json


def form_str(key, vals, simbol=' '):
    val = json.dumps(vals[key]).strip('"')
    return f'  {simbol} {key}: {val}\n'
