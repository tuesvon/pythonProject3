# 2.5.2
print(23 // 7)
print(20 // 5)
print(2 // 5)
print(123 // 10)
print(-123 // 10)

# 2.5.3
print(23 % 7)
print(20 % 5)
print(2 % 5)
print(123 % 10)

# 2.5.4
a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)

# 2.5.5
a = 82 // 3 ** 2 % 7
print(a)

# 2.5.6 / Геометрическая прогрессия
b = int(input())
q = int(input())
n = int(input())
bn = b * q ** (n - 1)
print(bn)

# 2.5.7 / Расстояние в метрах
a = int(input())
print(a // 100)

# 2.5.8 / Мандарины
n = int(input())
k = int(input())
a = k // n
b = k % n
print(a)
print(b)

# 2.5.9 / Сама неотвратимость
n = int(input()) + 1
print(n // 2)

# 2.5.10 / Номер купе
n = int(input())
print(-(n // -4))

# 2.5.11 / Пересчет временного интервала
m = int(input())
hh = m // 60
mm = m % 60
print(m, 'мин - это', hh, 'час', mm, 'минут.')

# 2.5.12 / Обработка цифр числа
num = 17
a = num % 10
b = num // 10
print(a)
print(b)
print()
num = 754
a = num % 10
b = (num % 100) // 10
c = num // 100
print(a)
print(b)
print(c)
print()

# Задача 1. Напишите программу, определяющую число десятков и единиц в двузначном числе.
num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Число десятков =', first_digit)
print('Число единиц =', last_digit)

# Задача 2. Напишите программу, в которой рассчитывается сумма цифр двузначного числа.
num = int(input())
a = num % 10
b = num // 10
print('Сумма цифр =', a + b)

# Задача 3. Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа.
num = int(input())
a = num % 10
b = num // 10
print('Искомое число =', a * 10 + b)

# Задача 4. Напишите программу, в которую вводится трёхзначное число и которая выводит на экран его цифры (через запятую).
num = int(input())
a = num % 10
b = (num // 10) % 10
c = num // 100
print(c, b, a, sep=',')

# 2.5.13 / Трехзначное число
num = int(input())
a = num % 10
b = (num // 10) % 10
c = num // 100
s = a + b + c
p = a * b * c
print('Сумма цифр =', s)
print('Произведение цифр =', p)

# 2.5.14 / Перестановка цифр
# num = int(input())
a = num % 10
b = (num // 10) % 10
c = num // 100
print(c, b, a, sep='', end='\n')
print(c, a, b, sep='', end='\n')
print(b, c, a, sep='', end='\n')
print(b, a, c, sep='', end='\n')
print(a, c, b, sep='', end='\n')
print(a, b, c, sep='', end='\n')

# 2.5.15 / Четырехзначное число
num = int(input())
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10
print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)

# 2.5.16 / расставить по порядку
n = 12345
a = n // 10000
b = n % 10000 // 1000
c = n % 1000 // 100
d = n % 100 // 10
e = n % 10
print('Первая цифра', a)
print('Вторая цифра', b)
print('Третья цифра', c)
print('Четвёртая цифра', d)
print('Пятая цифра', e)
