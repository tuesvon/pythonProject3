#Три города

city1 = input()
city2 = input()
city3 = input()

ls1 = len(city1)
ls2 = len(city2)
ls3 = len(city3)

if ls1 <= ls2 and ls1 <= ls3:
    print(city1)
elif ls2 <= ls1 and ls2 <= ls3:
    print(city2)
else:
    print(city3)

if ls1 >= ls2 and ls1 >= ls3:
    print(city1)
elif ls2 >= ls1 and ls2 >= ls3:
    print(city2)
else:
    print(city3)