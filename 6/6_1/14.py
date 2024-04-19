#Интересное число

x = int(input())
a = x // 100
b = x % 100 // 10
c = x % 10
y = max(a, b, c)
z = min(a, b, c)
w = (a + b + c) - (y + z)
if w == y - z:
    print("Число интересное")
else:
    print("Число неинтересное")
