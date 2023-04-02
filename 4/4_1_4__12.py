# 4.1.4 / Пароль
password_first = input()
password_second = input()
if password_second == password_first:
    print('Пароль принят')
else:
    print('Пароль не принят')

# 4.1.5 / Четное или нечетное
num = int(input())
if num % 2 == 0:
   print('Четное')
else:
   print('Нечетное')

# 4.1.6 / Соотношение
num = int(input())
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10
if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')

# 4.1.7 / Роскомнадзор
age = int(input())
if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

# 4.1.8 / Арифметическая прогрессия
a = int(input())
b = int(input())
c = int(input())
if c == (b - a) + b:
    print('YES')
else:
    print('NO')

# 4.1.9 / Наименьшее из двух чисел
a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)

# 4.1.10 / Наименьшее из четырех чисел
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b:
    z = a
else:
    z = b
if c < d:
    x = c
else:
    x = d
if z < x:
    print(z)
else:
    print(x)

# 4.1.11 / Возрастная группа
age = int(input())
if age <= 13:
    print('детство')
if 14 <= age <= 24:
    print('молодость')
if 25 <= age <= 59:
    print('зрелость')
if 60 <= age:
    print('старость')

# 4.1.12 / Только +
a = int(input())
b = int(input())
c = int(input())
if a > 0:
    a = a
else:
    a = 0
if b > 0:
    b = b
else:
    b = 0
if c > 0:
    c = c
else:
    c = 0
if a + b + c > 0:
    print(a + b + c)
else:
    print('0')
