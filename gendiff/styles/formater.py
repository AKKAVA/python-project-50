from gendiff.styles import stylish
from gendiff.styles import plain
from gendiff.styles import json_formater


def style(style_name: str, diff: dict) -> str:
    if not style_name or style_name == 'stylish':
        styled_diff = stylish.stylish(diff)
    elif style_name == 'plain':
        styled_diff = plain.plain(diff)
    elif style_name == 'json':
        styled_diff = json_formater.json_formater(diff)
    else:
        raise ValueError(f"{style_name} style not suppoted")
    return styled_diff.rstrip('\n')
