mushrooms = []
mushroom = input('Введите название гриба, который вы собрали: \n')

while mushroom != '0':
    mushrooms.append(mushroom)
    mushroom = input('Введите название гриба, который вы собрали: \n')


print('Грибы, которые вы собрали: ')
for mushroom in mushrooms:
    print(mushroom)