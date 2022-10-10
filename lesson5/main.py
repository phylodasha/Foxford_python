# print('Привет, новый пользователь!')
# name = input('Как тебя зовут?\n')

# guess_number = 4
# count_try = 3

# print(f'Еще раз здравствуй, {name}! Цель игры: угадать число, загаданное компьютером!')
# print('У тебя есть три попытки, чтобы угадать это число!')
# print('Число загадано!')
# player_number = int(input('Как думаете, какое число загадано? \n'))
# count_try = count_try - 1
# if player_number == guess_number:
#     print('Молодец! Ты угадал число!')
# else:
#     print('Ты не угадал :(')
#     print(f'Ты уже использовал {3 - count_try} попыток')
#     print(f'У тебя осталось {count_try} попыток')
#     player_number = int(input('Как думаете, какое число загадано? \n'))
#     count_try = count_try - 1
#     if player_number == guess_number:
#         print('Молодец! Ты угадал число!')
#     else:
#         print('Ты не угадал :(')
#         print(f'Ты уже использовал {3 - count_try} попыток')
#         print(f'У тебя осталось {count_try} попыток')
#         player_number = int(input('Как думаете, какое число загадано? \n'))
#         count_try = count_try - 1
#         if player_number == guess_number:
#             print('Молодец! Ты угадал число!')
#         else:
#             print('Ты не угадал :(')
#             print(f'Ты уже использовал {3 - count_try} попыток')
#             print(f'У тебя осталось {count_try} попыток')


a = 1
b = a + 2
c = b + 3
b = c - b
if a >= b:
    print(f"a + b = {a+b}")
elif a >= c:
    print(f"a + b = {a+c}")
else:
    print(f"c + b = {c+b}")  