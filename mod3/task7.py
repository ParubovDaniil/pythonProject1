phone_number = input()
cleaned_number = ''.join(char for char in phone_number if char.isdigit() or char == '+')
print(cleaned_number)