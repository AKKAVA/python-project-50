from .scripts import scripts as scripts

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

    for key in data_1:
        if key in data_2:

            if data_1[key] == data_2[key]:
                if isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
                    diff.update({
                        key: {
                            STATUS: NESTED,
                            VALS: compare_data(data_1[key], data_2[key])
                        }
                    })
                else:
                    diff.update({
                        key: {
                            STATUS: UNCHANGED,
                            VALS: data_1[key]
                        }
                    })
            else:
                if isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
                    diff.update({
                        key: {
                            STATUS: NESTED,
                            VALS: compare_data(data_1[key], data_2[key])
                        }
                    })
                else:
                    vals_1, vals_2 = data_1[key], data_2[key]

                    if isinstance(vals_1, dict):
                        vals_1 = compare_data(vals_1, vals_1)

                    if isinstance(vals_2, dict):
                        vals_2 = compare_data(vals_2, vals_2)

                    diff.update({
                        key: {
                            STATUS: CHANGED,
                            VALS: {
                                FIRST_FILE_VAL: vals_1,
                                SECOND_FILE_VAL: vals_2
                            }
                        }
                    })
        else:
            if isinstance(data_1[key], dict):
                diff.update({
                    key: {
                        STATUS: REMOVED,
                        VALS: compare_data(data_1[key], data_1[key])
                    }
                })
            else:
                diff.update({
                    key: {
                        STATUS: REMOVED,
                        VALS: data_1[key]
                    }
                })

    for key in data_2:
        if key not in data_1:
            if isinstance(data_2[key], dict):
                diff.update({
                    key: {
                        STATUS: ADDED,
                        VALS: compare_data(data_2[key], data_2[key])
                    }
                })
            else:
                diff.update({
                    key: {
                        STATUS: ADDED,
                        VALS: data_2[key]
                    }
                })

    diff = scripts.sort_diff_by_key(diff)

    return diff
