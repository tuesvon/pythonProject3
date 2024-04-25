# Квадратное уравнение**

import math

a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("Нет корней")