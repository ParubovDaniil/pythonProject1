# Получаем номер телефона от пользователя
phone_number = input("Введите номер телефона: ")

# Приводим номер телефона к нужному формату
allowed_chars = '0123456789+'
formatted_phone_number = ''

for digit in phone_number:
    if digit in allowed_chars:
        formatted_phone_number += digit

print(formatted_phone_number)