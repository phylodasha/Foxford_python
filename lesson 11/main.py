# def greet_user():
#     name = input('Введите ваше имя!')
#     print(f'Привет, {name}! Добро пожаловать в Фоксфорд!')


# greet_user()

# def max(a, b):
#     if a > b:
#         print(f'{a} больше {b}')
#     elif b > a:
#         print(f'{b} больше {a}')
#     else:
#         print('Числа равны')
# first_number = 11
# second_number = 10
# third_number = 8
# fourth_number = 5
# max(third_number, first_number)


def print_numbers(first_number, last_number, step):
    for i in range(first_number, last_number, step):
        print(f'Число {i}')


print_numbers(1, 10, 2)