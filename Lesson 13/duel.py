import random
import time

start = 0 # эта переменная засекает время
finish = 0
counter = 0
error = 0
answer = 0
first = 0
second = 0

while counter != 3 and error != 3:
    first = random.randint(1, 100)
    second = random.randint(1, 100)

    print(f'Чему равна сумма {first} и {second}')
    start = time.time()
    answer = int(input())
    finish = time.time()

    print(f'Вы ответили на вопрос за {finish - start} секунд')

    if answer == first+second and finish - start < 10:
        counter += 1
        print('Отличная работа!')
        print(f'Количество ваших баллов: {counter}')
        print(f'Количество ошибок: {error}')

    else:
        error += 1
        print('К сожалению, неверно')
        print(f'Количество ошибок: {error}')


if counter == 3:
    print('Поздравляю с победой')
else:
    print('Ты проиграл(')