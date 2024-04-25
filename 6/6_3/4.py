# Средние значения

import math

a = float(input())
b = float(input())

arif = (a + b) / 2
geom = math.sqrt(a * b)
garm = (2 * a * b) / (a + b)
kvadr = math.sqrt((a**2 + b**2) / 2)

print(arif)
print(geom)
print(garm)
print(kvadr)