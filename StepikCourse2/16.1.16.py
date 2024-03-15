def pretty_print(args, side='-', delimeter='|'):
    symbols = [i for i in args]
    pretty_line = delimeter + ' '
    for i in symbols:
        pretty_line += f'{i} {delimeter} '
    print(f' {side*(len(pretty_line) - 3)}')
    print(pretty_line)
    print(f' {side*(len(pretty_line) - 3)}')


pretty_print([1, 2, 10, 23, 123, 3000], side='*')