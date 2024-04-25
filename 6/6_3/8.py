# Правильный многоугольник
import math

n = float(input())
a = float(input())

s = (n * a ** 2) / (4 * math.tan(math.pi / n))
print(s)