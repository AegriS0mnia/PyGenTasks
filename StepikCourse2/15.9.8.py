def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    result = any(map(lambda key_word: key_word in command, ignore))

    return result

