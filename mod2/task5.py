# Ввод доменного имени
domain = input("Введите доменное имя: ")

# Инициализация переменных для домена и доменного расширения
domain_name = ""
extension = ""

# Поиск доменного расширения
i = len(domain) - 1
while domain[i] != '.':
    extension = domain[i] + extension
    i -= 1

# Поиск первой части домена
j = i - 1
while j >= 0 and domain[j] != '.':
    domain_name = domain[j] + domain_name
    j -= 1

# Поиск поддомена, если есть
subdomain = ""
if j > 0:
    k = j - 1
    while k >= 0 and domain[k] != '.':
        subdomain = domain[k] + subdomain
        k -= 1

# Вывод домена и доменного расширения
print(extension)
print(domain_name)
if subdomain:
    print(subdomain)