with open('goats.txt', encoding='utf-8') as goats, open('answer.txt', 'w', encoding='utf-8') as answer:

    lines = [i.strip() for i in goats]
    colours = [i for i in lines[1: lines.index('GOATS')]]
    lines = lines[lines.index('GOATS') + 1:]
    goats_count = {}
    goats_in_total = len(lines)

    for colour in colours:
        goats_count.setdefault(colour, lines.count(colour))

    for i in goats_count:
        if goats_count[i] % 100 > 7:
            print(i, file=answer)