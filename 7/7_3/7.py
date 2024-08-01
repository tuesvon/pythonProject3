# Асимптотическое приближение

import math

n = int(input())
a = 0
for i in range(1, n + 1):
    a += 1 / i
log_n = math.log(n)
print(a - log_n)