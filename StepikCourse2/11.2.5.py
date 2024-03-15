def merge(dicts):
    keys = {}
    result_dict = {}
    for _dict in dicts:
        for key in _dict:
            keys.setdefault(key, [])

    keys = sorted(keys)
    for key in keys:
        set_of_values = set()
        for _dict in dicts:
            for _key in _dict:
                if _key == key:
                    set_of_values.add(_dict[_key])
        result_dict.setdefault(key, set_of_values)

    return result_dict
