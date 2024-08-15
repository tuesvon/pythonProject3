i = 0
while i < 10:
    print(i, 'меньше 10')
    i += 1
print(i, 'равно 10')

num = int(input())
while num != -1:
    print("Квадрат числа", num, "равен:", num * num)
    num = int(input())

# Считывание данных до стоп значения
text = input()
total = 0
while text != 'stop':
    total += int(text)
    text = input()
print('Сумма чисел равна:', total)


#Бесконечный цикл
i = 0
total = 0
while i < 10:
    total += i