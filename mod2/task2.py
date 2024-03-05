side_length = int(input())

perimeter = side_length * 4
area = side_length ** 2
diagonal = (2 ** 0.5) * side_length

print("{:.2f}, {:.2f}, {:.2f}".format(perimeter, area, diagonal))


