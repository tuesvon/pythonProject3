# 4_3_3 // Гонка спидстеров
n = int(input())
k = int(input())
if n > k:
    print('NO')
elif n < k:
    print('YES')
elif n == k:
    print("Don't know")

# 4_3_4 // Вид треугольника
a, b, c = int(input()), int(input()), int(input())
if a == b != c or a == c != b or a != b == c:
    print('Равнобедренный')
elif a == b == c:
    print('Равносторонний')
elif a != b != c:
    print('Разносторонний')

# 4_3_5 // Среднее число
a, b, c = int(input()), int(input()), int(input())
if c > b > a or a > b > c:
    print(b)
elif c > a > b or b > a > c:
    print(a)
else:
    print(c)

# 4_3_6 // Количество дней
a = int(input())
if a == 2:
    print('28')
elif (a == 4) or (a == 6) or (a == 9) or (a == 11):
    print('30')
else:
    print('31')

# 4_3_7 // Церемония взвешивания
a = int(input())
if a < 60:
    print('Легкий вес')
elif 60 <= a < 64:
    print('Первый полусредний вес')
elif 64 <= a < 69:
    print('Полусредний вес')

# 4_3_8 // Самописный калькулятор
a, b = int(input()), int(input())
c = input()
if c == '*':
    print(a * b)
elif c == '-':
    print(a - b)
elif c == '+':
    print(a + b)
elif c == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')

# 4_3_9 // Цветовой микшер
a, b = input(), input()
if (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
    print('фиолетовый')
elif (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
    print('оранжевый')
elif (a == 'синий' and b == 'желтый') or (a == 'желтый' and b == 'синий'):
    print('зеленый')
elif (a == 'синий' and b == 'синий') or (a == 'красный' and b == 'красный') or (a == 'желтый' and b == 'желтый'):
    print(a)
else:
    print('ошибка цвета')

# 4_3_10 // Цвета колеса рулетки
a = int(input())
if a == 0:
    print('зеленый')
elif 1 <= a <= 10:
    if a % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= a <= 18:
    if a % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= a <= 28:
    if a % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= a <= 36:
    if a % 2 == 0:
        print('красный')
    else:
        print('черный')
else:
    print('ошибка ввода')

# 4_3_11 // Пересечене отрезков
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (b1 < a2) or (b2 < a1):
    print('пустое множество')
elif b1 == a2:
    print(b1)
elif b2 == a1:
    print(b2)
elif a1 <= a2 < b1 < b2:
    print(a2, b1)
elif a2 <= a1 < b2 < b1:
    print(a1, b2)
elif a1 < a2 < b2 <= b1:
    print(a2, b2)
elif a2 < a1 < b1 <= b2:
    print(a1, b1)
elif a1 == a2 and b1 == b2:
    print(a1, b1)