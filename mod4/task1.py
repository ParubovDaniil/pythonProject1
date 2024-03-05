def check_numbers(numbers):
    unique_numbers = set(numbers)

    if len(unique_numbers) == 1:
        print("Все числа равны")
    elif len(unique_numbers) == len(numbers):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")


# Считываем список чисел через пробел и преобразуем его в список целых чисел
input_numbers = input("Введите список чисел через пробел: ").split()
numbers = [int(num) for num in input_numbers]


check_numbers(numbers)