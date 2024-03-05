user_input = input("Введите натуральное число: ")
a = (f"{int(user_input):b} {int(user_input):o} {int(user_input):X}") if user_input.isdigit() and int(user_input) > 0 else "Неверный ввод"
print(a)