#Сортировка трёх

a = int(input())
b = int(input())
c = int(input())
x = max(a, b, c)
z = min(a, b, c)
y = (a + b + c) - (x + z)
print(x, y, z, sep="\n")