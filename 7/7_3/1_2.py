# Вычисление суммы и произведения

total = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        total = total + num

print('Сумма чисел больших 10 равна',  total)