def triangle():
    stars = 15
    lines = []
    for i in range(8):
        line = ' ' * i + '*' * stars
        stars -= 2
        lines.append(line)
    print(*lines[::-1], sep='\n')

triangle()