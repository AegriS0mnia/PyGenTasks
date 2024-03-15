numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

list_len = len(numbers)
last_element = numbers[-1]
reversed_list = numbers[::-1]
is_5_17_in_list = 5 in numbers and 17 in numbers
_5_17_answer = 'NO'
if is_5_17_in_list:
    answer = 'YES'
cuted_list = numbers[1:len(numbers) - 1]

print(list_len, last_element, reversed_list, _5_17_answer, cuted_list, sep='\n')