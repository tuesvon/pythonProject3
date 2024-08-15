# Сумма чисел

num = int(input())
count = 0
while num >= 0:
    count += num
    num = int(input())

print(count)