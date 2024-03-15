string = input()

new_string = string[len(string)//2 + len(string) % 2:] + string[:len(string)//2 + len(string) % 2]
print(new_string)
