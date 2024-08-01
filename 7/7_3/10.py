# Без нулей

counter = 1
for _ in range(10):
    num = int(input())
    if num != 0:
        counter *= num
print(counter)