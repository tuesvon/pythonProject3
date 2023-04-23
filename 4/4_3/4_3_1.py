# x = int(input())
# y = int(input())
# if x > 0:
#     if y > 0:
#         print('Первая четверть')
#     else:
#         print('Четвертая четверть')
# else:
#     if y > 0:
#         print('Вторая четверть')
#     else:
#         print('Третья четверть')

# grade = int(input('Введите вашу отметку по 100-балльной системе: '))
# if grade >= 90:
#     print(5)
# else:
#     if grade >= 80:
#         print(4)
#     else:
#         if grade >= 70:
#             print(3)
#         else:
#             if grade >= 60:
#                 print(2)
#             else:
#                 print(1)

grade = int(input('Введите вашу отметку: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)