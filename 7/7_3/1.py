# Подсчет количества

counter = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        counter = counter + 1
print("Было введено", counter, "чисел, больших 10")
print("-----")

counter1 = 0
counter2 = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1

print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.' )
print('-----')

counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1
print(counter)
print("-----")

# Вычисление суммы и произведения
total = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        total = total + num
print('Сумма чисел больших 10 равна',  total)
print("-----")