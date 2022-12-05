# def even_or_not(a):
#     if a % 2 == 1:
#         print('Нечетное')
#     else:
#         print('Четное')

# number = int(input('Введите число '))
# even_or_not(number)



# импорт модуля random
# import random

# print(random.randint(1, 100))

# a = ['мандарин1', 'мандарин2', 'мандарин3', 'мандарин4', 'мандарин5', 'мандарин6']
# print(random.choice(a))

import time


start = time.time()

for i in range(100000):
    print('hello!')

finish = time.time()
print(f'Время выполнения программы: {finish - start}')
