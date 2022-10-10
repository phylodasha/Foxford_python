
from random import *

import time


price = 99

def newprint(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()


n_products = int(input('Введите количество товаров:\n  '))

n_packages = int(input ('Введите количество пакетов:\n  '))

newprint('Мазагин ВСЕ ПО 99')
time.sleep(1.7)

newprint('КАССОВЫЙ ЧЕК')



newprint('=' * 75)



newprint(f'Количество пакетов: {n_packages}')

newprint(f'Количество товаров {n_products}')

sum_= price*n_products + n_packages
discount = 0


if    500 < (price*n_products + n_packages) < 1500:
    discount = 5
    print('Скидка: 5%')
if    1500 < (price*n_products + n_packages) < 5000:
    discount = 10
    print('Скидка: 10%')
if    5000 < (price*n_products + n_packages) < 15000:
    discount = 20
    print('Скидка: 20%')
if  15000 < (price*n_products + n_packages) > 20000:
    print('Скидка: 50%')
    discount = 50


gh = 5

print(f'ИТОГО: {sum_ * ((100-discount)/100)}')

mark1 = int(input('Здравствуйте! Оцените работу нашего магазина по шкале от 1 до 5: \n'))

if mark1 > gh:
 print('Это больше 5!')
 discount = 0

if mark1 > gh:
   mark1 = int(input(' Оцените работу нашего магазина по шкале от 1 до 5: \n')) 


time.sleep(1)
mark2 = int(input('Здравствуйте! Оцените работу нашего магазина по шкале от 1 до 5: \n'))

if mark2 > gh:
 print('Это больше 5!')
 discount = 0

if mark2 > gh:
   mark2 = int(input(' Оцените работу нашего магазина по шкале от 1 до 5: \n')) 

time.sleep(1)
mark3 = int(input('Здравствуйте! Оцените работу нашего магазина по шкале от 1 до 5: \n'))

if mark3 > gh:
 print('Это больше 5!')
discount = 0
if mark3 > gh:
   mark3 = int(input(' Оцените работу нашего магазина по шкале от 1 до 5: \n')) 

time.sleep(1)
mark4 = int(input('Здравствуйте! Оцените работу нашего магазина по шкале от 1 до 5: \n'))

if mark4 > gh:
 print('Это больше 5!')
discount = 0
if mark4 > gh:
   mark4 = int(input(' Оцените работу нашего магазина по шкале от 1 до 5: \n')) 

time.sleep(1)
newprint(f'Оценка пользователя 1: {mark1}') 

time.sleep(1)
newprint(f'Оценка пользователя 2: {mark2}')

time.sleep(1)
newprint(f'Оценка пользователя 3: {mark3}')

time.sleep(1)
newprint(f'Оценка пользователя 4: {mark4}')



time.sleep(1)
avg = (mark1 + mark2+ mark3 + mark4)/4
time.sleep(1)
newprint('Высчитываю среднюю оценку....')

time.sleep(1.5)

print('.....')

time.sleep(1.6)

print('......')

time.sleep(1.6)

newprint('Средняя оценка')
print(avg)


