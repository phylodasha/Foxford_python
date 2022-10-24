from random import*
import time



def newprint(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.02)
    print()


guess_number = randint(1, 5)
print(guess_number)

count_try = 3

name = input('Как вас зовут? \n')
time.sleep(1)
newprint('Сейчас Рандомайзер выберет число От 1 до 5, ваша задача отгадать это число')
time.sleep(0.5)





newprint(f'У вас будет {count_try} попытки. ')
time.sleep(0.7)

time.sleep(2)
newprint('Число загадано, угадывайте! ')
time.sleep(1)


    

count_try -= 1
player_number = int(input('Введите число: '))
while player_number != guess_number and count_try > 0:
     if player_number >= guess_number:
      newprint('Это число больше загаданного')
     if player_number <= guess_number:
      newprint('Это число меньше загадонного')
    
     newprint('Ответ неверный:( Попробуй ещё раз!')
    
     time.sleep(1)

     newprint(f'Потрачено попыток: {3 - count_try}')
     time.sleep(1)
     newprint(f'Осталось попыток: {count_try}')
     time.sleep(1)
     player_number = int(input('Введите число: '))
     count_try -= 1
time.sleep(0.5)

if player_number != guess_number:
        newprint(f'Вы проиграли, правильный ответ: {player_number}')
if player_number == guess_number:

    newprint('....')
    time.sleep(1)
    newprint('Молодец! ты угадал(а) число!')    
time.sleep(2)
