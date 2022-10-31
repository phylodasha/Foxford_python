from cmath import atan
from random import *
import time
import os
from colorama import *
import pickle

init()

def newprint(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()



f = 0

Xp = 0

Player_Level = 1

Player_Damage = 0

Enemy_Damage1 = 0

Player_Block = 0

Enemy1_HP = 0

War = 0

Class = 0

a = randint(2,15)

next = 0

language = 'Языки:'

heal = 100

inventory = []


os.system('CLS')


newprint(Style.BRIGHT + 'Dark Forest')
newprint('\n1 - Начать \n2 - Продолжить \n3 - Помощь/Настройки \n4 - Выйти ')
start = input()

while start == '3':
    os.system('CLS')
    newprint('\nИнструкция важных клавиш:')
    newprint('Если вы устали или не хотите больше играть, то просто нажмите 0 и вы выйдите и сохраните свой прогресс')
    
    time.sleep(3)
    os.system('CLS')
    newprint(Style.BRIGHT + 'Dark Forest')
    newprint('\n1 - Начать \n2 - Продолжить \n3 - Помощь/Настройки \n4 - Выйти ')
    start = input()


if start == '1':
    os.system('CLS')
    newprint('\nВыбирите уровень сложности')
    newprint('\n1 - Легко \n2 - Нормально \n3 - Сложно')
    hard = input()

if hard == '1' :
    os.system('CLS')
    newprint('\nЗагрузка...')
    a = randint(3,15)
    time.sleep(a)
    os.system('CLS')
    newprint('\nПриветствую вас')
    time.sleep(1.5)
    newprint('\nВыбирите свой класс')
    newprint('\n1 - Воин \n2 - Стерелок \n3 - Маг')
    f = 15
    Class = input()

elif hard == '2' :
    os.system('CLS')
    newprint('\nЗагрузка...')
    a = randint(3,15)
    time.sleep(a)
    os.system('CLS')
    newprint('\nПриветствую вас')
    time.sleep(1.5)
    newprint('\nВыбирите свой класс')
    newprint('\n1 - Воин \n2 - Стерелок \n3 - Маг')
    f = 25
    Class = input()

elif hard == '3' :
    os.system('CLS')
    newprint('\nЗагрузка...')
    a = randint(3,15)
    time.sleep(a)
    os.system('CLS')
    newprint('\nПриветствую вас')
    time.sleep(1.5)
    newprint('\nВыбирите свой класс')
    newprint('\n1 - Воин \n2 - Стерелок \n3 - Маг')
    f = 30
    Class = input()

if Class == '1':
    newprint('\nВоин прекрасный выбор')
    time.sleep(2)
    newprint('\nДавайте мы вас снарядим')
    inventory += ['Ржавый меч ', 'Потрепаная кольчуга ', 'Морковь. ']
    newprint(Fore.GREEN + '\nВы получили:')
    newprint(Fore.YELLOW + '+ Ржавый меч,\n + Потрепаная кольчуга,\n + Морковь.' + Style.RESET_ALL)
    time.sleep(3)
    newprint('\nНу что отправляемся?')
    newprint('\n1 - Да \n2 - Нет')
    Yes = input()

elif Class == '2':
    newprint('\nЛюди которые метко стреляют никогда не помешают')
    time.sleep(2)
    newprint('\nДавайте мы вас снарядим')
    inventory += ['Ржавый меч ', 'Потрепаная кольчуга ', 'Морковь. ']
    newprint(Fore.GREEN + '\nВы получили:')
    newprint(Fore.YELLOW + '+ Ржавый меч,\n + Потрепаная кольчуга,\n + Морковь.' + Style.RESET_ALL)
    time.sleep(3)
    newprint('\nНу что отправляемся?')
    newprint('\n1 - Да \n2 - Нет')
    Yes = input()

elif Class == '3':
    newprint('\nС мудрым человеком всегда есть о чем поговорить')
    time.sleep(2)
    newprint('\nДавайте мы вас снарядим')
    inventory += ['Ржавый меч ', 'Потрепаная кольчуга ', 'Морковь. ']
    newprint(Fore.GREEN + '\nВы получили:')
    newprint(Fore.YELLOW + '+ Ржавый меч,\n + Потрепаная кольчуга,\n + Морковь.' + Style.RESET_ALL)
    time.sleep(3)
    newprint('\nНу что отправляемся?')
    newprint('\n1 - Да \n2 - Нет')
    Yes = input()

    

if Yes == '1':
    newprint('\nХорошо в путь!')
    os.system('CLS')
    newprint('\nКуда отправимся?')
    newprint('\n 1 - Лес ')
    put = input()

else:
    newprint(Style.BRIGHT + 'Хорошо жду'+ Style.RESET_ALL)
    time.sleep(5)
    newprint('\nНу что отправляемся?')
    newprint('\n1 - Да')
    Yes = input()

    if Yes == '1':
        newprint('\nХорошо в путь!')
        os.system('CLS')
        newprint('\nКуда отправимся?')
        newprint('\n 1 - Лес ')
        put = input()





if put == '1':
    newprint('Хорошо отправляемся в лес')
    os.system('CLS')
    time.sleep(3)
    newprint('\nСмотрите это же волк надо бы обойти его как вы считаете?')
    newprint('\n1 - Да давайте обойдём \n2 - Нет нечего боятся каких то волков идем на пролом')
    answer1 = input()

if answer1 == '1':
    os.system('CLS')
    time.sleep(2)
    newprint('\nУх... Мы упешно прошли без драки')
    newprint(Fore.GREEN + '\nВы получили:')
    newprint(Fore.YELLOW + '+ 1 очко скрытности\n + 15 xp' + Style.RESET_ALL)
    Xp += 15

if answer1 == '2':
    os.system('CLS')
    newprint('Сражение начнетса через:')
    time.sleep(1)
    os.system('CLS')
    newprint('3')
    time.sleep(1)
    os.system('CLS')
    newprint('2')
    time.sleep(1)
    os.system('CLS')
    newprint('1')
    time.sleep(1)
    os.system('CLS')
    newprint(Fore.GREEN + f'\nXP - {heal}' )
    newprint(Fore.RED + f'\nEnemy HP 50')
    newprint('\n1 - Атака \n2 - Блок \n3 - Уворот')
    atack = input()

War = 1
Enemy1_HP = 50

while War == 1:
    if heal <= 0:
        newprint('\nВы погибли')
        time.sleep(3)
        newprint('\nКонец игры')
        break

    elif Enemy1_HP <= 0:
        newprint('Враг повержен вы победили')
        break
    if atack == '1':
        if heal <= 0:
            newprint('\nВы погибли')
            time.sleep(3)
            newprint('\nКонец игры')
            break

        elif Enemy1_HP <= 0:
                newprint('Враг повержен вы победили')
                break
        Player_Damage = randint(1,20)
        Enemy_Damage1 = randint(0,f)
        newprint(f'Вы нанесли урона {Player_Damage}\n')
        Enemy1_HP -= Player_Damage
        newprint(f'Вам нанесли урона {Enemy_Damage1}\n')
        os.system('CLS')
        heal -= Enemy_Damage1
        newprint(Fore.GREEN + f'\nXP - {heal}' )
        newprint(Fore.RED + f'\nEnem HP {Enemy1_HP}')
        newprint('\n1 - Атака \n2 - Блок \n3 - Уворот')
        if heal <= 0:
            newprint('\nВы погибли')
            time.sleep(3)
            newprint('\nКонец игры')
            break

        elif Enemy1_HP <= 0:
                newprint('Враг повержен вы победили')
                break
        atack = input()

    elif atack == '2':
        if heal <= 0:
            newprint('\nВы погибли')
            time.sleep(3)
            newprint('\nКонец игры')
            break

        elif Enemy1_HP <= 0:
                newprint('Враг повержен вы победили')
                break
        Player_Block = randint(10,f)
        Enemy_Damage1 = randint(0,f)
        newprint(f'\nВам нанесли урона {Enemy_Damage1}')
        newprint(f'\nВы парировали {Player_Block}')
        os.system('CLS')
        Enemy_Damage1 -= Player_Block
        if Enemy_Damage1 >= 0:
            heal -= Enemy_Damage1
            newprint(Fore.GREEN + f'\nXP - {heal}' )
            newprint(Fore.RED + f'\nEnem HP {Enemy1_HP}')
            newprint('\n1 - Атака \n2 - Блок \n3 - Уворот')
            atack = input()
        else:
            newprint(Fore.GREEN + f'\nXP - {heal}' )
            newprint(Fore.RED + f'\nEnem HP {Enemy1_HP}')
            newprint('\n1 - Атака \n2 - Блок ')
            if heal <= 0:
                newprint('\nВы погибли')
                time.sleep(3)
                newprint('\nКонец игры')
                break

            elif Enemy1_HP <= 0:
                newprint('Враг повержен вы победили')
                break
            atack = input()


        