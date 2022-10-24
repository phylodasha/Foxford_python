word = 'автомобиль'
task = 'Что вы выиграете, если отгадаете слово?'
letter_number = 1
count_try = 3

print('Приветствую нового игрока! Сейчас мы сыграем в игру Поле Чудес')
print(f'Тема текущего раунда: {task}')
print(f'Слово состоит из {len(word)} букв')
print(f'{word[0]} ' + (len(word)-1) * '_ ')

while letter_number < len(word):
    letter = input(f'Введите букву номер {letter_number+1}: ')
    if letter == word[letter_number]:
        print('Верно! Крутите барабан и называйте следующую букву!')
        letter_number += 1
    else:
        print('Не верно!')
        count_try -= 1
        print(f'Осталось попыток: {count_try} ')

    if count_try == 0:
        print('У вас закончились попытки! Приходите в другой раз!')
        break

    print(f'{word[0:letter_number]} ' + (len(word)-letter_number) * '_ ')

if count_try > 0:
    print('И вы выигрываете аааавтомобиль!!!')