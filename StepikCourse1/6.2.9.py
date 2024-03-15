str1, str2, str3 = input(), input(), input()

str1_len, str2_len, str3_len = len(str1), len(str2), len(str3)

min_len = min(str1_len, str2_len, str3_len)
max_len = max(str1_len, str2_len, str3_len)
average_len = ((str1_len + str2_len + str3_len) - (max_len + min_len))

if average_len - min_len == max_len - average_len:
    print('YES')
else:
    print('NO')
