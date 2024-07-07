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

            if isinstance(val, dict):
                val = compare_data(val, val)

            diff.update(build_node(key, REMOVED, val))
            continue

        if key not in data_1:
            val = data_2[key]

            if isinstance(val, dict):
                val = compare_data(val, val)

            diff.update(build_node(key, ADDED, val))
            continue

        if isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
            val_1, val_2 = data_1[key], data_2[key]
            val = compare_data(val_1, val_2)
            diff.update(build_node(key, NESTED, val))
            continue

        if data_1[key] == data_2[key]:
            val = data_1[key]
            diff.update(build_node(key, UNCHANGED, val))
            continue

        if data_1[key] != data_2[key]:
            val_1, val_2 = data_1[key], data_2[key]

            if isinstance(val_1, dict):
                val_1 = compare_data(val_1, val_1)

            if isinstance(val_2, dict):
                val_2 = compare_data(val_2, val_2)

            val = {
                FIRST_FILE_VAL: val_1,
                SECOND_FILE_VAL: val_2
            }

            diff.update(build_node(key, CHANGED, val))
            continue

    return diff


def build_node(key, status, vals) -> dict:
    node = {key: {
        STATUS: status,
        VALS: vals
    }}

    return node
