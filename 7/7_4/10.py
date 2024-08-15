text = input()
total = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    total += 1
    text = input()
print(total)