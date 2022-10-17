n = int(input('Сколько пользователей будут участвовать в опросе? \n'))
count = 0
sum_ = 0
while count < n:
    grade = int(input('Как вы оцениваете работу нашего магазина?'))
    sum_ += grade
    count += 1

print('Средняя оценка: ', sum_/n)
