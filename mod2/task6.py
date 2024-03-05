input_string = input("Введите строку из символов '0' и '1': ")

zeros = 0
ones = 0

for char in input_string:
    if char == '0':
        zeros += 1
    elif char == '1':
        ones += 1

if zeros == ones:
    print('yes')
else:
    print('no')