# Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным
num = int(input())
if 100 <= num <= 999:
    print('Число трёхзначное')
else:
    print('Число не трёхзначное')

# Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
if a != b and a != c and b != c:
    print("Числа различны")
else:
    print("Есть одинаковые числа")

# Напишите программу, которая по координатам точки, не лежащей на осях координат,
# определяет номер координатной четверти, в которой она находится.
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("1 четверть")
if x < 0 and y > 0:
    print("2 четверть")
if x < 0 and y < 0:
    print("3 четверть")
if x > 0 and y < 0:
    print("4 четверть")