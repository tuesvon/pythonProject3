# оператор and
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
if age >= 12 and grade >= 7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')


# оператор or
city = input('В каком городе вы живете?: ')
if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

# оператор not
age = int(input('Сколько вам лет?: '))
if not (age < 12):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

