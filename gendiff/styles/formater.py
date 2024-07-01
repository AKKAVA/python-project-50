from gendiff.styles import stylish as stylish
from gendiff.styles import plain as plain
from gendiff.styles import json_formater as json_formater


def get_style(style_name):
    if not style_name or style_name == 'stylish':
        return stylish.stylish
    elif style_name == 'plain':
        return plain.plain
    elif style_name == 'json':
        return json_formater.json_formater
    else:
        raise ValueError(f"{style_name} style not suppoted")
