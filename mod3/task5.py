words = input().split()
result = ''.join(word[-1] for word in words)
print(result)