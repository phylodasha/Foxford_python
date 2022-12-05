import random

print('Введите количество участников: ')
kol = int(input())
winner = random.randint(1, kol)
print(f'Победитель - число {winner}')