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


def plain(diff: dict, path: list = []):
    res = str()

    for key, value in diff.items():

        status, vals = value[STATUS], value[VALS]

        if status == NESTED:
            cur_path = form_path(path, key)
            res += plain(vals, cur_path)

        elif status in (CHANGED, REMOVED, ADDED):
            cur_path = form_path(path, key)
            # if cur_path:
            #     formed_path = '.'.join(cur_path)
            # else:
            #     formed_path = key
            formed_path = '.'.join(cur_path)

            if status == CHANGED:
                vals_1, vals_2 = vals[FIRST_FILE_VAL], vals[SECOND_FILE_VAL]
                vals_1, vals_2 = format_val(vals_1), format_val(vals_2)
                res += f"Property '{formed_path}' was updated. From {vals_1} to {vals_2}\n"
            
            elif status == ADDED:
                vals = format_val(vals)
                res += f"Property '{formed_path}' was added with value: {vals}\n"
            
            elif status == REMOVED:
                res += f"Property '{formed_path}' was removed\n"
    return res


def format_val(val):
    if isinstance(val, dict):
        return '[complex value]'
    return json.dumps(val).replace('"', "'")


def form_path(path, key):
    if not path:
        return [key,]
    tmp = [_ for _ in path]
    tmp.append(key)
    return tmp
