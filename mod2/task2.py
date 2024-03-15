# На вход подается длина стороны квадрата, рассчитать периметр, площадь и диагональ с
# округлением до 2 знака.
# Формат ввода
# 9
# Формат вывода
# 36.00, 81.00, 12.73


side = float(input())

perimetr = side * 4
rounded_perimetr = round(perimetr, 2)

square = side * side
rounded_square = round(square, 2)

diagonal_square = side * (2**0.5)
rounded_diagonal_square = round(diagonal_square,2)

print (f"{rounded_perimetr:.2f}, {rounded_square:.2f}, {rounded_diagonal_square:.2f}")


