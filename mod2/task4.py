# Для введенного в десятичном коде натурального числа найти представление в двоичном,
# восьмеричном и шестнадцатеричном кодах. Если введено не натуральное число, вывести
# диагностику: «Неверный ввод». Использовать встроенные возможности языка python
# запрещено.
# Формат ввода
# 100
# Формат вывода
# 1100100, 144, 64

user_input = input ("Введите натуральное десятичное число: ")
number = int(user_input)
while number < 0:
    print("Введенное число не натурнольное. Введите еще раз")
    user_input = input("Введите натуральное десятичное число: ")
    number = int(user_input)

binary = ""
octal = ""
hexadecimal = ""

numforbinary = number
numforoctal = number
numforhexadecimal = number



while numforbinary > 0:
    binary = str(numforbinary % 2) + binary
    numforbinary = numforbinary // 2


while numforoctal > 0:
    octal = str(numforoctal % 8) + octal
    numforoctal = numforoctal // 8


# здесь используется функция ord, которая возвращает числовое представление символа ASCII, переданного в качестве аргумента.
# В данном случае мы берем ASCII-код символа 'A' (который равен 65) и добавляем к нему остаток от деления remainder, вычитая 10.
# Это преобразует остаток в числовое значение символа в диапазоне от 10 до 15. Затем функция chr преобразует числовое значение обратно в символ ASCII.

while numforhexadecimal > 0:
    remainder = numforhexadecimal % 16
    if remainder < 10:
        hexadecimal = str(remainder) + hexadecimal
    else:
        hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
    numforhexadecimal = numforhexadecimal // 16


print(f"{binary}, {octal}, {hexadecimal}")