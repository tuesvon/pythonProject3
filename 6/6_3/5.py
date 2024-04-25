# Тригонометрическое выражение
import math

x = float(input())
r = (x * math.pi) / 180
a = math.sin(r) + math.cos(r) + math.tan(r)**2
print(a)