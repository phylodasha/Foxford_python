from random import*

input('Введите ваше имя: ')
count_try = 3
question = 'Попробуй угадать число от 1 до 20, которое загадал вредный Числик)'
right_answer = randint(1, 20)
print(question)
player_answer = input('\nкакое число? ')
count_try -=1
while player_answer!=right_answer and count_try > 0:
    print('Попробуй еще раз!')
    if count_try == 1:
        print(f'У тебя осталось {count_try} попытка')
    else:
        print(f'У тебя осталось {count_try} попытки')
    print(question)
    player_answer = input('\nВаш ответ: ')
    count_try -= 1
    if right_answer == player_answer:
          print('Поздравляю с победой!') 
          print(f'Вы использовали {3 - count_try} из 3 попыток')
if player_answer!=right_answer:
        print(f'Вы проиграли, правильный ответ: {right_answer}')