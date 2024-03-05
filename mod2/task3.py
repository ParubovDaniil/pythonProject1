# Считываем три целых числа
input_str = input().strip()

# Ищем первое число
first_space_index = input_str.index(' ')
a = int(input_str[:first_space_index])

# Обрезаем строку передвигаясь на один символ за первым числом
rest_str = input_str[first_space_index + 1:]

# Ищем второе число
second_space_index = rest_str.index(' ')
b = int(rest_str[:second_space_index])

# Третье число - все оставшееся
c = int(rest_str[second_space_index + 1:])

# Определяем число, стоящее посередине
middle_number = a
if (b <= a <= c) or (c <= a <= b):
    middle_number = a
elif (a <= b <= c) or (c <= b <= a):
    middle_number = b
else:
    middle_number = c

print(middle_number)