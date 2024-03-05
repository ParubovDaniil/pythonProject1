domain = input("Введите доменное имя сайта: ")
a = (f"{'\n'.join(domain.split('.')[::-1])}")
print(a)