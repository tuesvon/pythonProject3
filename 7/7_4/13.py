# Количество пятёрок

num = int(input())
count = 0
while 5 >= num > 0:
    if num == 5:
        count += 1
    num = int(input())
print(count)