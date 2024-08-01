# Наибольшие числа

n = int(input())
largest_1 = 0
largest_2 = 0

for _ in range(n):
    lar1 = int(input())
    if lar1 > largest_1:
        largest_2 = largest_1
        largest_1 = lar1
    elif lar1 > largest_2 and lar1 != largest_1:
        largest_2 = lar1


print(largest_1)
print(largest_2)