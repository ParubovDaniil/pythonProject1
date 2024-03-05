input_data = input()

s = ""
i = ""
comma_found = False

for char in input_data:
    if char == ',':
        comma_found = True
    elif comma_found:
        i += char
    else:
        s += char

index = 0
result = 0

while index < len(s) and s[index:] == i + s[index + len(i):]:
    result += 1
    index += len(i)

print(result)