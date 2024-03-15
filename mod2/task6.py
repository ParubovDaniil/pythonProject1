# Строка состоит из 0 и 1 Выведите ‘yes’, если количество единиц совпадает с
# количеством нулей. И ‘no’ в противном случае.
# Пример 1
# Ввод
# 01011111101100111101
# Вывод
# no

user_input = input("Введите двоичное число: ")

num = ""
counter_of_units = 0
zero_counter = 0

for char in user_input:
    if char == '1':
        counter_of_units = int (counter_of_units + 1)
    else:
        zero_counter += 1

if counter_of_units == zero_counter:
    print("yes")
else:
    print("no")