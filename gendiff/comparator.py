# STATUSES
UNCHANGED = 'UNCHANGED'
CHANGED = 'CHANGED'
REMOVED = 'REMOVED'
ADDED = 'ADDED'
NESTED = 'NESTED'

# DICT KEYS
STATUS = 'STATUS'
VALS = 'VALS'

# VALS KEYS
FIRST_FILE_VAL = 'FIRST_FILE_VAL'
SECOND_FILE_VAL = 'SECOND_FILE_VAL'


def compare_data(data_1: dict, data_2: dict) -> dict:
    diff = dict()

    keys_1, keys_2 = set(data_1.keys()), set(data_2.keys())
    keys = sorted(keys_1 | keys_2)

    for key in keys:

        if key not in data_2:
            val = data_1[key]

            diff.update(build_node(key, REMOVED, val))

        elif key not in data_1:
            val = data_2[key]

            diff.update(build_node(key, ADDED, val))

        elif isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
            val_1, val_2 = data_1[key], data_2[key]
            val = compare_data(val_1, val_2)
            diff.update(build_node(key, NESTED, val))

        elif data_1[key] == data_2[key]:
            val = data_1[key]
            diff.update(build_node(key, UNCHANGED, val))

        elif data_1[key] != data_2[key]:
            val = {
                FIRST_FILE_VAL: data_1[key],
                SECOND_FILE_VAL: data_2[key]
            }
            diff.update(build_node(key, CHANGED, val))

    return diff


def build_node(key, status, vals) -> dict:
    node = {key: {
        STATUS: status,
        VALS: vals
    }}

    return node
