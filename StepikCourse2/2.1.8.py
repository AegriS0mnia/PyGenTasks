number = int(input())
digits_chunks = []

while number >= 1000:
    last_3 = str(number)[-3:]
    digits_chunks.append(last_3)
    number //= 1000
else:
    digits_chunks.append(str(number))

print(','.join(digits_chunks[::-1]))
