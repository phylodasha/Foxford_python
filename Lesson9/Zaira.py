print('Приветствую умного нового игрока!')
player_name = input('Введите свое имя: ')

print('------Правила игры------')
print('Добро пожаловать в суперигру "Поле чудес"')
print('Ваша задача : вводить по одному символу загаданных слов в порядке возрастания порядкового номера(первым слово с наименьшим порядковым номером) ')
print('Важно вводить буквы в порядке возрастания и в нижнем регистре')

word1 = 'прямая'
word_len1 = len(word1)
word2 = 'парабола'
word_len2 = len(word2)
word3 = 'кубическая парабола'
word_len3 = len(word3)
word4 = 'гипербола'
word_len4 = len(word4)

print('Удачи!')

print('Отправляемся к первому слову!')
print('Первое задание : назовите график функции y=x')
print(f'Первое слово состоит из {word_len1} букв')

count_try = 4
letter_number1 = 1
print(f'{word1[0:letter_number1]}{(word_len1 - letter_number1)*"_"}')
while count_try >=0:
    letter = input(f'Введите {letter_number1+1}-ю букву: ')
    if letter == word1[letter_number1]:
        print('Вы угадали!')
        letter_number1 += 1
    else:
        count_try -= 1
        print('Вы не угадали :_(')
    if letter_number1 == word_len1:
        break
    print(f'{word1[0:letter_number1]}{(word_len1 - letter_number1)*"_"}')
if count_try < 0:
    print('Вы проиграли!')
    raise SystemExit
else:
    print(f'{player_name}, молодец! Отлично! Отправляемся к следующему второму слову!')

print('Второе задание : назовите график функции y=x^2')
print(f'Второе слово состоит из {word_len2} букв')

count_try = 4
letter_number2 = 1
print(f'{word2[0:letter_number2]}{(word_len2 - letter_number2)*"_"}')
while count_try >=0:
    letter = input(f'Введите {letter_number2+1}-ю букву: ')
    if letter == word2[letter_number2]:
        print('Вы угадали!')
        letter_number2 += 1
    else:
        count_try -= 1
        print('Вы не угадали :_(')
    if letter_number2 == word_len2:
        break
    print(f'{word2[0:letter_number2]}{(word_len2 - letter_number2)*"_"}')
if count_try < 0:
    print('Вы проиграли!')
    raise SystemExit
else:
    print(f'{player_name}, блестяще! До победы осталось совсем немного! Отправляемся к следующему третьему словосочетанию!')

print('Третье задание : назовите график функции y=x^3')
print(f'Третье словосочетание состоит из {word_len3} символов')

count_try = 4
letter_number3 = 1
print(f'{word3[0:letter_number3]}{(word_len3 - letter_number3)*"_"}')
while count_try >=0:
    letter = input(f'Введите {letter_number3+1}-ю букву: ')
    if letter == word3[letter_number3]:
        print('Вы угадали!')
        letter_number3 += 1
    else:
        count_try -= 1
        print('Вы не угадали :_(')
    if letter_number3 == word_len3:
        break
    print(f'{word3[0:letter_number3]}{(word_len3 - letter_number3)*"_"}')
if count_try < 0:
    print('Вы проиграли!')
    raise SystemExit
else:
    print(f'{player_name}, молодец! Так держать! До победы осталось совсем немного! Отправляемся к четвёртому слову!')

    print('Четвёртое задание : назовите график функции y=k/x')
    print(f'Четвёртое слово состоит из {word_len4} букв')

    count_try = 4
letter_number4 = 1
print(f'{word4[0:letter_number4]}{(word_len4 - letter_number4)*"_"}')
while count_try >=0:
    letter = input(f'Введите {letter_number4+1}-ю букву: ')
    if letter == word4[letter_number4]:
        print('Вы угадали!')
        letter_number4 += 1
    else:
        count_try -= 1
        print('Вы не угадали :_(')
    if letter_number4 == word_len4:
        break
    print(f'{word4[0:letter_number4]}{(word_len4 - letter_number4)*"_"}')
if count_try < 0:
    print('Вы проиграли!')
else:
    print(f'Перед нами победитель! И это - {player_name}! Поздравляем!')