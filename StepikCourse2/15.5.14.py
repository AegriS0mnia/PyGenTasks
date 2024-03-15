def func_apply(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)
    return result

