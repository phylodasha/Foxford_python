guess_word = 'лис'
count_try = 3

name = input('Как вас зовут? ')
print('Сейчас компьютер загадет слово. Ваша задача - это слово отгадать')
print('Подсказка: Именно к этому виду животных относится Мистер Фокс')

print(f'У вас будет {count_try} попыток. ')
print('Компьютер загадал слово. Угадывайте!')
player_word = input('Введите слово: ')
count_try -= 1
while player_word != guess_word and count_try > 0:
    print('Ответ неверный :( Попробуйте еще раз!')
    print(f'Потрачено {3 - count_try} попыток')
    print(f'Осталось попыток: {count_try}')
    player_word = input('Введите  слово: ')
    count_try -= 1

if player_word == guess_word:
    print('Молодец! Ты угадал число!')
else:
    print('Попробуй сыграть в другой раз!')



