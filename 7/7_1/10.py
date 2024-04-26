# Популяция

m = int(input())
p = int(input())
n = int(input())

for i in range(1):
    print(i + 1, m)

for i in range(2, n + 1):
    m = m + m * p / 100
    print(i, m)

