user_input = input("Введите три целых числа a, b, c через пробел: ")

# Извлекаем числа из строки
a = ''
b = ''
c = ''
number = ''
number_index = 0

for char in user_input:
    if char != ' ':
        number += char
    else:
        if number_index == 0:
            a = int(number)
        elif number_index == 1:
            b = int(number)
        elif number_index == 2:
            c = int(number)
        number_index += 1
        number = ''

# Обработка последнего числа
if number_index == 2:
    c = int(number)
else:
    b = int(number)

# Проверка условий ввода
while a < -1000 or c > 1000:
    print("Число A должно быть больше или равно -1000, а число C должно быть меньше или равно 1000. Попробуйте снова.")
    user_input = input("Введите три целых числа a, b, c через пробел: ")

    a = ''
    b = ''
    c = ''
    number = ''
    number_index = 0

    for char in user_input:
        if char != ' ':
            number += char
        else:
            if number_index == 0:
                a = int(number)
            elif number_index == 1:
                b = int(number)
            elif number_index == 2:
                c = int(number)
            number_index += 1
            number = ''

    # Обработка последнего числа
    if number_index == 2:
        c = int(number)
    else:
        b = int(number)

# Упорядочивание чисел
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

# Находим число, которое будет стоять между двумя другими
middle_number = b

print("Число, стоящее между числами a и c:", middle_number)