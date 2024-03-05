def fast_power(base, power):
    if power == 0:
        return 1
    elif power % 2 == 0:
        return fast_power(base * base, power // 2)
    else:
        return base * fast_power(base, power - 1)

# Считываем два числа через пробел и преобразуем их в целые числа
a, n = map(int, input("Введите два числа через пробел (a n): ").split())

result = fast_power(a, n)
print(f"{a} в степени {n} = {result}")