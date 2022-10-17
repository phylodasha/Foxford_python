n = int(input('Сколько пользователей будут участвовать в опросе? \n'))
count = 0
sum_ = 0
while count < n:
    grade = int(input('Как вы оцениваете работу нашего магазина?'))
    if grade > 5 or grade < 0:
        print('Выставляей оценки от 1 до 5 включительно!')
    else:
        sum_ += grade
        count += 1

print('Средняя оценка: ', sum_/n)
