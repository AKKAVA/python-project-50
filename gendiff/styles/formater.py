from gendiff.styles import stylish as stylish
from gendiff.styles import plain as plain


def get_style(style_name):
    if not style_name:
        return stylish.stylish
    elif style_name == 'plain':
        return plain.plain
    else:
        raise ValueError(f"{style_name} style not suppoted")
