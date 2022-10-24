import random
print('Я загадала целое число от 0 до 10. Угадай с 5 попыток!')
chislo=random.randrange(10)
popitka_count=0
while popitka_count<=4:
    popitka_count+=1
    popitka=int(input('Это число:'))
    if popitka<chislo:
        print('Больше!')
    elif popitka>chislo:
        print('Меньше!')
    else:
        print('Ничего себе! Ты отгадал! Это правда',chislo)
        print('Количество попыток:',popitka_count)
        break
if popitka_count==5 and popitka!=chislo:
    print('О, ужас! Ты совершенно не умеешь читать мои мысли!\n\
Так и не смог угадать число за 5 попыток :(')