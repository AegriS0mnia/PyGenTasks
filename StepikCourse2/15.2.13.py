def greet(name, *args):
    greeting = f'Hello, {name}'

    for names in args:
        greeting += f' and {names}'

    return greeting + '!'


print(greet('Ruslan', 'Timur'))