def to_binary(n):
    if n <= 0:
        return '0'

    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


def to_octal(n):
    if n <= 0:
        return '0'

    octal = ''
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    return octal


def to_hexadecimal(n):
    if n <= 0:
        return '0'

    hexadecimal = ''
    while n > 0:
        remainder = n % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder - 10 + ord('A')) + hexadecimal
        n //= 16
    return hexadecimal


# Ввод числа
num_str = input()
try:
    num = int(num_str)
    if num <= 0:
        print('Неверный ввод')
    else:
        binary = to_binary(num)
        octal = to_octal(num)
        hexadecimal = to_hexadecimal(num)
        print(binary + ', ' + octal + ', ' + hexadecimal)
except ValueError:
    print('Неверный ввод')