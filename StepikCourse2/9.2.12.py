number_of_charts = int(input())
nerds = set()

for i in range(number_of_charts):
    chart_len = int(input())
    chart = {input() for i in range(chart_len)}

    if nerds == set():
        nerds = nerds | chart
    nerds = nerds & chart

print(*sorted(nerds), sep='\n')