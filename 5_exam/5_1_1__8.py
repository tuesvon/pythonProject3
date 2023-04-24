# 5_1_1 // Начало столетия
a = int(input())
c = (a // 10) % 10
d = a % 10
if c == 0 and d == 0:
    print('YES')
else:
    print('NO')

# 5_1_2 // Шахматная доска
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
z = (x1 + y1 + x2 + y2) % 2
if z == 0:
    print('YES')
else:
    print('NO')

# 5_1_3 // Girls only
a = int(input())
g = input()
if 10 <= a <= 15 and g == 'f':
    print('YES')
else:
    print('NO')

# 5_1_4 // Римские цифры
n = int(input())
if n == 1:
    print('I')
elif n == 2:
    print('II')
elif n == 3:
    print('III')
elif n == 4:
    print('IV')
elif n == 5:
    print('V')
elif n == 6:
    print('VI')
elif n == 7:
    print('VII')
elif n == 8:
    print('VIII')
elif n == 9:
    print('IX')
elif n == 10:
    print('X')
else:
    print('ошибка')

# 5_1_5 // YES or NO вот в чем вопрос
n = int(input())
if n % 2 != 0:
    print('YES')
elif 2 <= n <= 5 and n % 2 == 0:
    print('NO')
elif 6 <= n <= 20 and n % 2 == 0:
    print('YES')
elif n % 2 == 0 and n > 20:
    print('NO')

# 5_1_6 // Ход слона
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 + y1) == (x2 + y2) or (x1 - y1) == (x2 - y2):
    print('YES')
else:
    print('NO')

# 5_1_7 // Ход коня
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x1 - x2 == 2 and y1 - y2 == -1:
    print('YES')
elif x1 - x2 == 1 and y1 - y2 == -2:
    print('YES')
elif x1 - x2 == -1 and y1 - y2 == -2:
    print('YES')
elif x1 - x2 == -2 and y1 - y2 == -1:
    print('YES')
elif x1 - x2 == 2 and y1 - y2 == 1:
    print('YES')
elif x1 - x2 == 1 and y1 - y2 == 2:
    print('YES')
elif x1 - x2 == -1 and y1 - y2 == 2:
    print('YES')
elif x1 - x2 == -2 and y1 - y2 == 1:
    print('YES')
else:
    print('NO')

# 5_1_8 // Ход ферзя
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x1 == x2 or y1 == y2:
    print('YES')
elif (x1 + y1) == (x2 + y2) or (x1 - y1) == (x2 - y2):
    print('YES')
else:
    print('NO')

