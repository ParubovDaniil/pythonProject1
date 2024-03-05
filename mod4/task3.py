def euclidean_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)

# Ввод двух чисел
a, b = map(int, input("Введите два числа через пробел (a, b): ").split())

# Вызываем функцию для нахождения НОД
result = euclidean_gcd(a, b)

print(f"Наибольший общий делитель чисел {a} и {b} равен: {result}")