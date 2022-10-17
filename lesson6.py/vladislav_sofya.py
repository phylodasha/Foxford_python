from multiprocessing.connection import wait
from random import *
import time 
import os 



def newprint(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

os.system('clear')




newprint('\n\nЧтобы начать разговор с Фросей напишите "Привет".')
newprint('Если вы уже общались с Фросей то скажите "Фрося"\n')
newprint('\nЧтобы Фрося вас легче понимала пишите грамотно')
hi = input()

if hi == 'Привет':
    name = input(newprint('\nЗдравствуйте я Фрося, а как вас зовут?'))
    time.sleep(1)
    newprint(f'\nРада познакомиться {name}')

elif hi == 'привет':
    name = input(newprint('\nЗдравствуйте я Фрося, а как вас зовут?'))
    time.sleep(1)
    newprint(f'\nРада познакомиться {name}')

a = ['Как настроение?', 'Вы любите смотреть фильмы?', 'Какой цвет радуги вам нравиться?', 'У тебя есть питомец?', 'Хотите сыграть?']

randomgame = ['Камень, ножницы, бумага',]

whait = choice(a)

Vampus = 0
    
vampusstart = ['Охотник(ца) в местной таверне ходят слухе о страных звуков из пещеры на востоке', 'Вас нанял глава деревни чтобы вы нашли и поймали монстра из пещер на востоке', 'Идет сильный дождь вы были около пещеры и решили туда пойти']

game1 = 0

stone = ['Камень', 'Ножницы', 'Бумага']

player = 0

game = 0

yes = 0

if whait == 'Как настроение?':
    newprint('\nКак настроение?')
    vopros1 = input()
    if vopros1 == 'Хорошо':
        newprint('\nЭто замечательно')
        whait = choice(a)
    elif vopros1 == 'хорошо':
        newprint('\nЭто замечательно')
        whait = choice(a)
    elif vopros1 == 'Отлично':
        newprint('\nУ меня тоже')
        whait = choice(a)
    elif vopros1 == 'Нормально':
        newprint('\nЭто лучше чем плохо')
        whait = choice(a)
    elif vopros1 == 'Плохо':
        newprint('\nНу не грусти посылаю тебе лучи счастья')
        whait = choice(a)
    elif vopros1 == 'отлично':
        newprint('\nУ меня тоже')
        whait = choice(a)
    elif vopros1 == 'нормально':
        newprint('\nЭто лучше чем плохо')
        whait = choice(a)
    elif vopros1 == 'плохо':
        newprint('\nНу не грусти посылаю тебе лучи счастья')
        whait = choice(a)
    else:
        newprint('\nПохоже вы сделали опечатку или я не распознала ваш ответ напишите его пожалуйста еще раз')
        vopros1 = input()


if whait == 'Вы любите смотреть фильмы?':
    newprint('\nВы любите смотреть фильмы?')
    vopros2 = input()

    if vopros2 == 'Да':
        newprint('\nЯ тоже')
        whait = choice(a)

    elif vopros2 == 'Нет':
        newprint('\nЖалко')
        whait = choice(a)

    elif vopros2 == 'да':
        newprint('\nЯ тоже')
        whait = choice(a)

    elif vopros2 == 'нет':
        newprint('\nЖалко')
        whait = choice(a)

    else:
        newprint('\nПохоже вы сделали опечатку или я не распознала ваш ответ напишите его пожалуйста еще раз')
        vopros2 = input()


if whait == 'Какой цвет радуги вам нравиться?':
    newprint('Какой цвет радуги вам нравиться?')
    vopros3 = input()

    if vopros3 == 'Красный':
        newprint('\nПрекрасный цвет, как Рэд из Angry birds)')
        whait = choice(a)
    elif vopros3 == 'красный':
        newprint('\nПрекрасный цвет, как Рэд из Angry birds)')
        whait = choice(a)
    elif vopros3 == '\nОранжевый':
        newprint('\nКрасивый цвет, как медок')
        whait = choice(a)
    elif vopros3 == 'оранжевый':
        newprint('\nКрасивый цвет, как медок')
        whait = choice(a)
    elif vopros3 == 'Желтый':
        newprint('\nПрекрасный цвет, как Чак из Angry birds') 
        whait = choice(a)       
    elif vopros3 == 'желтый':
        newprint('\nПрекрасный цвет, как Чак из Angry birds')
        whait = choice(a)
    elif vopros3 == 'Зеленый':
        newprint('\nПрекрасный по мнению биолога цвет, цвет хлорофилла')
        whait = choice(a)
    elif vopros3 == 'зеленый':
        newprint('\nПрекрасный по мнению биолога цвет, цвет хлорофилла')
        whait = choice(a)
    elif vopros3 == 'Голубой':
        newprint('\nЦвет неба)')
        whait = choice(a)
    elif vopros3 == 'голубой':
        newprint('\nЦвет неба)')  
        whait = choice(a)  
    elif vopros3 == 'Синий':
        newprint('\nЦвет гиацинтового ара)')
        whait = choice(a)
    elif vopros3 == 'синий':
        newprint('\nЦвет гиацинтового ара)')
        whait = choice(a)
    elif vopros3 == 'Фиолетовый':
        newprint('\nКак рейхан, такое фиолетовое растение')
        whait = choice(a)
    elif vopros3 == 'фиолетовый':
        newprint('\nКак рейхан, такое фиолетовое растение')
        whait = choice(a)
    elif vopros3 == 'Все':
        newprint('\nКак какая-нибудь Гульдова амадина или попугай)')
        whait = choice(a)
    elif vopros3 == 'все':
        newprint('\nКак какая-нибудь Гульдова амадина или попугай)')
        whait = choice(a)
    elif vopros3 == 'Никакой':
        newprint('\nСтранно)')
        whait = choice(a)
    elif vopros3 == 'никакой':
        newprint('\nСтранно)')
        whait = choice(a)
    else:
        newprint('\nПохоже вы сделали опечатку или я не распознала ваш ответ напишите его пожалуйста еще раз')
        vopros3 = input()

if whait == 'У тебя есть питомец?':
    newprint('У тебя есть питомец?')
    vopros4 = input()

    if vopros4 == 'Да':
        newprint('\nА какой?')
        input()
        newprint('\nПитомец это всегда хорошо')
        whait = choice(a)

    if vopros4 == 'да':
        newprint('\nА какой?')
        input()
        newprint('\nПитомец это всегда хорошо')
        whait = choice(a)
    

    if vopros4 == 'Нет':
        newprint('Жалко(')
        whait = choice(a)
    
    if vopros4 == 'нет':
        newprint('Жалко(')
        whait = choice(a)

    else:
        newprint('\nПохоже вы сделали опечатку или я не распознала ваш ответ напишите его пожалуйста еще раз')
        vopros4 = input()

if whait == '1':
    newprint('Вы можете задавать вопросы Фросе, а она вам.')
    newprint('\nЕщё вы можете поиграть с Фросей если скажите "Фрося давай сыграем" или "Давай сыграем (название игры)" например в "Охота на Вампуса"')
    newprint('Фрося выведет если она не может ответить на ваш вопрос')
    player = input()

while player == 'Как у тебя дела?':
    newprint('Замечательно а чего грустить)')

while player == 'Как у тебя дела':
    newprint('Замечательно а чего грустить)')

while player == 'как у тебя дела?':
    newprint('Замечательно а чего грустить)')

while player == 'как у тебя дела':
    newprint('Замечательно а чего грустить)')

while player == 'Фрося давай сыграем':
    game = random.choice(randomgame)
    newprint('С радостью ')
    newprint(f'Хотите сыграть в {game}')
    yes = input()
    if yes == 'Да':
        newprint('Хорошо включаю')
        if game == 'Камень, ножницы, бумага':
            game1 = 1

    elif yes == 'да':
        newprint('Хорошо включаю')
        if game == 'Камень, ножницы, бумага':
            game1 = 1

    elif yes == 'Нет':
        newprint('Ладно')

    elif yes == 'нет':
        newprint('Ладно')

while player == 'фрося давай сыграем':
    game = random.choice(randomgame)
    newprint('С радостью ')
    newprint(f'Хотите сыграть в {game}')
    yes = input()
    if yes == 'Да':
        newprint('Хорошо включаю')
        if game == 'Камень, ножницы, бумага':
            game1 = 1

    elif yes == 'да':
        newprint('Хорошо включаю')
        if game == 'Камень, ножницы, бумага':
            game1 = 1

    elif yes == 'Нет':
        newprint('Ладно')

    elif yes == 'нет':
        newprint('Ладно')

while game1 == 1:
    newprint('Хотите начать?')
    startgame1 = input()

    if startgame1 == 'Да':
        gamerandom = choice(stone)
        newprint('\nВведите "Камень" "Ножницы" или "Бумага"')
        playeruse = input()

        newprint(f'{gamerandom}')

        if playeruse == gamerandom:
            newprint('\nНичья')

        if playeruse == 'Камень':
            if gamerandom == 'Ножницы':
                newprint('\nВы победили')

            elif gamerandom == 'Бумага':
                newprint('\nВы проиграли')

        if playeruse == 'Ножницы':
            if gamerandom == 'Камень':
                newprint('\nВы проиграли')

            elif gamerandom == 'Бумага':
                newprint('\nВы победили')

        if playeruse == 'Бумага':
            if gamerandom == 'Ножницы':
                newprint('\nВы проиграли')

            elif gamerandom == 'Камень':
                newprint('\nВы победили')

    if startgame1 == 'да':
        gamerandom = choice(stone)
        newprint('\nВведите "Камень" "Ножницы" или "Бумага"')
        playeruse = input()

        newprint(f'{gamerandom}')

        if playeruse == gamerandom:
            newprint('\nНичья')

        if playeruse == 'Камень':
            if gamerandom == 'Ножницы':
                newprint('\nВы победили')

            elif gamerandom == 'Бумага':
                newprint('\nВы проиграли')

        if playeruse == 'Ножницы':
            if gamerandom == 'Камень':
                newprint('\nВы проиграли')

            elif gamerandom == 'Бумага':
                newprint('\nВы победили')

        if playeruse == 'Бумага':
            if gamerandom == 'Ножницы':
                newprint('\nВы проиграли')

            elif gamerandom == 'Камень':
                newprint('\nВы победили')

        if playeruse == 'Хватит':
            newprint('\nХорошо')
            game1 = 0

        if playeruse == 'хватит':
            newprint('\nХорошо')
            game1 = 0

if whait == 'Хотите сыграть?':
    newprint('Хотите сыграть?')
    yes = input()

    if yes == 'Да':
        newprint('Хорошо включаю')
        game1 = 1
        whait = 0

    elif yes == 'да':
        newprint('Хорошо включаю')
        game1 = 1
        whait = 0

    elif yes == 'Нет':
        newprint('Ладно')
        whait = choice(a)

    elif yes == 'нет':
        newprint('Ладно')
        whait = choice(a)        




