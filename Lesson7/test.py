import random

from random import randint
from turtle import hideturtle

print('Привет! Это мини-игра где нужно убивать монстров.')

health_p = randint(20, 35)
health_m = randint(30, 60)

print('Ты идешь по дороге и на тебя выпрыгивает монстр!')
print(f'У тебя {health_p} здоровья, а у монстра {health_m} ')

hit = int(input('Ты можешь ударить кулаком и монстр получит от 5 до 15 урона, для этого напиши 1. Либо атаковать с помощью меча и монстр получит от 15 до 30 урона , для этого напиши 2 \n'))

while health_p > 0:
    print(hit)
    fist_damage = randint(5, 15)
    arms_damage = randint(15, 30)
    damage_monstr = randint(10, 35)
    if hit == 1:
        print(f'Ты ударил монстра кулаком и он получил {fist_damage} урона.')
        health_m -= fist_damage
        hit = int(input('Ты можешь ударить кулаком и монстр получит от 5 до 15 урона, для этого напиши 1. Либо атаковать с помощью меча и монстр получит от 15 до 30 урона , для этого напиши 2 \n'))

    else:
        print(f'Ты атаковал монстра и он получил {arms_damage} урона.')
        health_m -= arms_damage
        hit = int(input('Ты можешь ударить кулаком и монстр получит от 5 до 15 урона, для этого напиши 1. Либо атаковать с помощью меча и монстр получит от 15 до 30 урона , для этого напиши 2 \n'))

    if health_m <= 0:
        print('Ты победил монстра! Молодец!')
        e = int(input('Хочешь продолжить? Да? Напиши 1. Нет? Тогда напиши 2. \n'))
        print(e)
        if e == 1:
            print('Тогда продолжим!')
        else:
            print('Пока!')
            break
    else:
        print(f'Продолжаем бой! Теперь атакует монстр. Он наносит тебе {damage_monstr} урона.')
        health_p -= damage_monstr
        print(f'Твоё здоровье теперь равно {health_p} ')
        if health_p <= 0:
            print('Ты умер :( Попробуй еще раз!')
            break
        else:
            print('Продолжим!')