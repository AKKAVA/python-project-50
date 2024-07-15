import json
from ..comparator import (
    UNCHANGED,
    CHANGED,
    REMOVED,
    ADDED,
    NESTED,
    STATUS,
    VALS,
    FIRST_FILE_VAL,
    SECOND_FILE_VAL
)


VALUE = 'VALS'


INDENT = ' '
INDENT_FOR_START = 2
INDENT_FOR_LEVEL = 4


def stylish(diff: dict, depth: int = 0,
            node_name: str = '', symbol: str = ' ') -> str:

    if not node_name:
        res = get_indent(depth) + '{\n'
    else:
        res = f'{get_indent(depth)}{symbol} {node_name}: {'{'}\n'

    for key, value in diff.items():
        try:
            status, vals = value[STATUS], value[VALS]
        except BaseException:
            status, vals = VALUE, value

        if status == NESTED:
            res += stylish(vals, depth + 1, key)

        elif status == VALUE:
            if isinstance(vals, dict):
                res += stylish(vals, depth + 1, key)
            else:
                res += format_row(key, vals, depth + 1)

        elif status == UNCHANGED:
            res += format_row(key, vals, depth + 1)

        elif status == CHANGED:

            symbol_1, symbol_2 = '-', '+'
            vals_1, vals_2 = vals[FIRST_FILE_VAL], vals[SECOND_FILE_VAL]

            if isinstance(vals_1, dict):
                res += stylish(vals_1, depth + 1, key, symbol_1)
            else:
                res += format_row(key, vals_1, depth + 1, symbol_1)

            if isinstance(vals_2, dict):
                res += stylish(vals_2, depth + 1, key, symbol_2)
            else:
                res += format_row(key, vals_2, depth + 1, symbol_2)

        elif status == REMOVED:
            symbol = '-'
            if isinstance(vals, dict):
                res += stylish(vals, depth + 1, key, symbol)
            else:
                res += format_row(key, vals, depth + 1, symbol)

        elif status == ADDED:
            symbol = '+'
            if isinstance(vals, dict):
                res += stylish(vals, depth + 1, key, symbol)
            else:
                res += format_row(key, vals, depth + 1, symbol)

    if not depth:
        res += get_indent(depth) + '}\n'
    else:
        res += get_indent(depth) + '  }\n'

    return res


def format_row(node_name, val, depth, symbol=' ') -> str:
    val = json.dumps(val).strip('"')
    return f'{get_indent(depth)}{symbol} {node_name}: {val}\n'


def get_indent(depth: int) -> str:
    return (depth * INDENT_FOR_LEVEL - INDENT_FOR_START) * INDENT
