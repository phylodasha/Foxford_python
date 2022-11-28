info = [5, 5, 3, 5, 4]
temp = [str(i) for i in info]
temp = ' '.join(temp)
print(f'Список ваших оценок: {temp}')

def add_grade(score):
    info.append(score)

def how_many(number):
    amount = 0
    for i in info:
        if i == number:
            amount += 1
    return amount

def sum_():
    summa = 0
    for i in info:
        summa += i
    return summa

def length():
    l = 0
    for i in info:
        l += 1
    return l

def average():
    return sum_()/length()
print('Привет, новый пользователь!')
while True:
    temp = [str(i) for i in info]
    temp = ' '.join(temp)
    print(f'Список ваших оценок: {temp}')
    print('Это бот, который поможет тебе уследить за школьными оценками')
    print('Введи 1, если хочешь добавить оценку в список')
    print('Введи 2, если хочешь посмотреть количество всех оценок')
    print('Введи 3, если хочешь посмотреть количество определенной оценки')
    print('Введи 4, если хочешь узнать среднюю оценку')
    print('введи 0, если захочешь выключить бота')
    answer = input('введи номер команды: ')
    if answer == '1':
        score = int(input('Введи оценку, которую нужно добавить: '))
        add_grade(score)
    elif answer == '2':
        print(length())
    elif answer == '3':
        score = int(input('Какие оценки нужно подсчитать? '))
        print(how_many(score))
    elif answer == '4':
        if len(info) < 1:
            print('Слишком мало оценок, добавьте еще!')
        else:
            print(average())
    elif answer == '0':
        break
    else:
        print('Такой команды нет')
