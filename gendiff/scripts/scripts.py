def sort_diff_by_key(diff: dict):
    res = dict()
    for key in sorted(diff.keys()):
        res.update({key: diff[key]})
    return res


def get_style(style_name):
    pass
