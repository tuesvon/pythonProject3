# 4_2_8 / Принадлежность 1
x = int(input())
if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

# 4_2_9 / Принадлежность 2
x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

# 4_2_10 / Принадлежность 3
x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

# 4_2_11 / Красивое число
x = int(input())
if 1000 <= x <= 9999 and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')

# 4_2_12 / Неравенство треугольника
a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')

# 4_2_13 / Високосный год
y = int(input())
if y % 4 == 0 and not y % 100 == 0 or y % 400 == 0:
    print('YES')
else:
    print('NO')

# 4_2_14 / Ход ладьи
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 == a2 or b1 == b2:
    print('YES')
else:
    print('NO')

# 4_2_15 / Ход короля
x = int(input())
y = int(input())
a2 = int(input())
b2 = int(input())
if a2 - 1 <= x <= a2 + 1 and b2 - 1 <= y <= b2 + 1:
    print('YES')
else:
    print('NO')