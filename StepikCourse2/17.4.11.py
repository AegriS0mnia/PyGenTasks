# with open('class_scores.txt', 'r+', encoding='utf-8') as class_scores:
#
#     scores = []
#     for line in class_scores:
#         line = line.split()
#         line[1] = int(line[1])
#         scores.append(line)
# for line in scores:
#     if line[1] <= 95:
#         line[1] += 5
#     else:
#         line[1] += 100 - int(line[1])
#
# with open('new_scores.txt', 'w', encoding='utf-8', newline='') as output:
#     for i in scores:
#         if i != scores[-1]:
#             print(*i, file=output)
#         else:
#             print(*i, file=output, end='')

with open('class_scores.txt') as class_scores, open('new_scores.txt', 'w') as new_scores:
    for line in class_scores:
        name, score = line.split()
        score = int(score) + 5
        if score > 100:
            score = 100
        print(name, score, file=new_scores)