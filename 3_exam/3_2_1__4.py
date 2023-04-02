# 3_2_1 / Звездный прямоугольник
print('*' * 17)
print('*', '*', sep=' ' * 15)
print('*', '*', sep=' ' * 15)
print('*' * 17)

# 3_2_2 / Сумма квадратов VS квадрат суммы
a = int(input())
b = int(input())
qs = (a + b)**2
sq = a**2 + b**2
print('Квадрат суммы', a, 'и', b, 'равен', qs)
print('Сумма квадратов', a, 'и', b, 'равна', sq)

# 3_2_3 / Большое число
a = int(input())
b = int(input())
c = int(input())
d = int(input())
q = a**b + c**d
print(q)

# 3_2_4 / Размножение n-ок
n = int(input())
a = n * 10 + n
b = n * 100 + a
sum = n + a + b
print(sum)