s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'


line_list = s.split()
lines_count = {}
most_frequent_lines = []

print(line_list)

for line in line_list:
     lines_count[line] = line_list.count(line)

for i in lines_count:
     if i == max(lines_count):
          most_frequent_lines.append()

print(lines_count)
print(most_frequent_lines)

