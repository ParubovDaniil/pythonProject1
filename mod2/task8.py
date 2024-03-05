words = input()

current_word = ''
current_char = ''
result = ''
is_space = False

for char in words:
    if char != ' ':
        current_char = char
        is_space = False
    else:
        is_space = True

    if is_space:
        result += current_word[-1]
        current_word = ''
    else:
        current_word += current_char

result += current_word[-1]

print(result)