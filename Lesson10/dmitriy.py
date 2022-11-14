from cmath import atan
from random import *
import time
import os
import pickle
import numpy
import random
from tkinter import *


def newprint(s):
  for letter in s:
    print(letter, end='', flush=True)
    time.sleep(0.04)
  print()
  return ""


def choice(inv, array, y=1):
  while True:
    if inv != '':
      newprint(inv)
    i = y - 1
    for element in array:
      i += 1
      string = f'{i}) {element}'
      newprint(string)
    chosen = input()
    if chosen.isdigit():
      chosen = int(chosen)
      if chosen in range(y, i + 1):
        return chosen
    newprint('Введите один из перечисленных вариантов')


titru = (
  '\nПродолжение следует!\nТитры:\nИдея игры - d1mkachoo\nПрограммист - d1mkachoo\nДизайнер - d1mkachoo'
)
a = 6
Key = 0
deystvie = 0
bigaptechka = 0
Secret = 0
ydarspider = random.randint(30, 45)
lovkost1 = random.randint(1, 10)
yron1 = random.randint(25, 30)
hpspider = random.randint(20, 25)
lovkost = 0
deystvie1 = 0
Key = 0
Player = 0
aptechka = 0
hp = 0
zombiehp = random.randint(30, 40)
Start = 0
Language = 0
newprint('Survival')
newprint('Нажмите "Enter" для продолжения')
input()
while Language != 1:
  Language = choice('Выбери язык', ['Русский', 'English'])
  if Language == 2:
    newprint('Извините но этот язык пока что не доступен')
name = input(newprint('Здравствуй новый игрок!\nНапиши свой ник'))
while Start != 1:
  Start = choice('', ['Начать игру', 'Титры', 'Код'])
  if Start == 2:
    newprint(
      'Идея игры - d1mkachoo\nПрограммист - d1mkachoo\nДизайнер - d1mkachoo')
  elif Start == 3:
    Secret = input(newprint('Здравствуйте!\nВведите код разработчика:'))
    if Secret != '5980':
      newprint('Код не подтверждён!')
    else:
      newprint('Код подтверждён\nЗдравствуй разработчик!\nКод игры через:')
      while a != 1:
        a = a - 1
        print(a)
        time.sleep(1)
      print('404\nИзвините но код игры доступен только для d1mkachoo!')
  elif Start == 1:
    newprint('Игра начинается!')
while Player != 1:
  Player = choice(f'{name} у тебя есть возможность выбрать бойца',
                  ['Боксёр', 'Стрелок'])
  if Player == 2:
    newprint('Извините но этот боец временно не доступен')
if Player == 1:
  hp = 100
  newprint(
    'Вы выбрали Боксёра!\nЭто хороший выбор\nВаши характеристики:\nУрон вблизи: 30\nХп: 100\nЛовкость: 10\nНажми "Enter" для продолжения'
  )
  input()
newprint(
  f'Поход начинается! {name}, вы оказались в заброшенной психушке, перед вами дверь, справа от вас ящик'
)
while Key != 1 or deystvie != 1:
  deystvie = choice(f'', ['Открыть дверь', 'Открыть ящик'])
  if deystvie == 1 and Key == 0:
    deystvie = (newprint(
      'Вы попробовали открыть дверь но она заперта (Подсказка: найдите ключ от двери)'
    ))
  if deystvie == 2 and Key != 1:
    deystvie = choice(
      'Вы открыли ящик и нашли в нём ключ (Подсказка: вы можете использовать ключ для открытия двери)',
      ['Открыть дверь', 'Открыть ящик'])
    Key = 1
  if deystvie == 2 and Key == 1:
    newprint('Вы уже обыскали этот ящик')
newprint('Дверь открыта!\nВы попали в коридор, вдали виднеется дверь')
deystvie = choice('', ['подойти к двери'], 3)
timer = time.time()
deystvie = choice(
  'Вы подошли к двери\nАААААААААААААА только не это тут зомби!\nОн идёт к вам!\nАтакуйте его первым, чтобы было больше шансов на победу!',
  ['атаковать'], 5)
timer = time.time() - timer
if timer > 10:
  ydar = random.randint(5, 10)
  hp = hp - ydar
  newprint(
    f'Зомби первый нанёс удар по вам (урон который вы получили {ydar}) у вас осталось {hp}хп'
  )
  lovkost = random.randint(1, 10)
else:
  lovkost = random.randint(1, 8)
while zombiehp > 0:
  yron = random.randint(25, 40)
  ydar = random.randint(10, 25)
  zombiehp = zombiehp - yron if yron < zombiehp else 0
  if lovkost == 1:
    newprint(
      f'Вы нанесли удар (урон который вы нанесли {yron}) у зомби осталось {zombiehp}хп\nЗомби ответил, но вы увернулись у вас осталось {hp}хп'
    )
  else:
    hp = hp - ydar
    newprint(
      f'Вы нанесли удар (урон который вы нанесли {yron}) у зомби осталось {zombiehp}хп\nЗомби нанёс удар по вам (урон который вы получили {ydar}) у вас осталось {hp}хп'
    )
  if zombiehp != 0:
    deystvie = choice('Нанесите ещё удар для победы', ['Атака!'], 5)
newprint(
  f'Поздравляем вы победили в этой битве! У вас осталось {hp}хп (Подсказка: вы можете находить предметы которые воcстанавливают вам здоровье)'
)
while Key != 2:
  deystvie = choice('Перед вами дверь, рядом лежит зомби',
                    ['Открыть дверь', 'Обыскать зомби'], 6)
  if deystvie == 7:
    deystvie = choice('Вы обыскали зомби и нашли у него ключ и бинты',
                      ['Использовать бинты'], 9)
    aptechka = 1
    Key = 2
  if deystvie == 6:
    deystvie = int(
      input(newprint('Вы попробовали открыть дверь, но она заперта')))
if aptechka == 1 and deystvie == 9:
  ph = random.randint(10, 15)
  hp = hp + ph
  deystvie = choice(
    f'Вы использовали бинты и восстановили себе {ph}хп теперь у вас {hp}хп',
    ['Открыть дверь'], 6)
newprint(
  'Вы открыли дверь!\nЗдесь большая комната\nсправа от вас коробка,слева тумбочка а перед вами дверь'
)
while True:
  deystvie1 = choice('', ['Открыть дверь', 'Обыск коробки', 'Обыск тумбочки'])
  if deystvie1 == 1 and Key != 4:
    deystvie1 = int(
      input(newprint('Вы попрбовали открыть дверь но она заперта')))
  if deystvie1 == 3 and Key < 3:
    deystvie1 = int(
      input(newprint('Вы попробовали открыть тумбочку но она заперта')))
  if deystvie1 == 2 and Key > 2:
    (newprint('Вы уже обыскали эту коробку'))
  if deystvie1 == 2 and Key < 3:
    newprint(
      'Вы открыли коробку и нашли ААААААААААА тут паук, он набросился на тебя, атакуй его быстрее!!'
    )
    while hpspider > 0:
      deystvie1 = choice('', ['Нанесите удар'], 5)
      hpspider = hpspider - yron1 if yron1 < hpspider else 0
      if lovkost1 == 1:
        newprint(
          f'Вы нанесли удар (урон который вы нанесли {yron1}) у паука осталось {hpspider}хп\nПаук не попал по вам, вы увернулись у вас осталось {hp}хп'
        )
      else:
        hp -= ydarspider
        newprint(
          f'Вы нанесли удар (урон который вы нанесли {yron1}) у паука осталось {hpspider}хп\nПаук нанёс удар по вам (урон который вы получили {ydarspider}) у вас осталось {hp}хп'
        )
    if hpspider != 0:
      ydarspider = random.randint(25, 40)
      newprint('Нанесите ещё удар для победы')
    if hpspider == 0 and Key == 2:
      newprint(
        f'Поздравляем вы победили в этой битве!У вас осталось {hp}хп, в коробке вы нашли ключ'
      )
      Key = 3
  if deystvie1 == 3 and Key == 3:
    deystvie1 = choice(
      f'Вы открыли тумбочку (ключ подошёл)\nВы нашли аптечку и ключ',
      ['Использовать аптечку'], 9)
    Key = 4
    if deystvie1 == 9:
      phbig = random.randint(20, 30)
      hp += phbig
      newprint(
        f'Вы использовали аптечку и восстановили себе {phbig}хп теперь у вас {hp}хп'
      )
  if deystvie1 == 3 and Key == 4:
    newprint('Вы уже обыскали эту тумбочку')
  if deystvie1 == 1 and Key == 4:
    newprint(f'Поздравляем вы выжили!{titru}')
    break
if hp <= 0:
  newprint(f'К сожаленю вы погибли! У вас не осталось хп({titru}')
