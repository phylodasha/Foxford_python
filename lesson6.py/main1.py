guess_number = 6
count_try = 3

name = input('Как вас зовут? ')
print('Сейчас компьютер загадет число. Ваша задача - это число отгадать')

print(f'У вас будет {count_try} попыток. ')
print('Компьютер загадал число. Угадывайте!')
player_number = int(input('Введите число: '))
count_try -= 1
while player_number != guess_number and count_try > 0:
    print('Ответ неверный :( Попробуйте еще раз!')
    print(f'Потрачено {3 - count_try} попыток')
    print(f'Осталось попыток: {count_try}')
    player_number = int(input('Введите число: '))
    count_try -= 1

if player_number == guess_number:
    print('Молодец! Ты угадал число!')
else:
    print('Попробуй сыграть в другой раз!')



