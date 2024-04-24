#Арифметические строки

num1 = len(input())
num2 = len(input())
num3 = len(input())

an = (2 * num2 - num3 - num1) * (2 * num3 - num2 - num1) * (2 * num1 - num2 - num3)

if an == 0:
    print("YES")
else:
    print("NO")
