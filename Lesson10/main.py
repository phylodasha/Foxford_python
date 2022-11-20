right_number = '543'
print('Привет, игрок! Твоя задача - отгадать число, которое я загадал!')
player_number = input('введи свое предположение: ')
while right_number != player_number:
    cows = 0 # коровы
    bulls = 0 # быки
    for player_symbol in range(len(player_number)):
        for right_symbol in range(len(right_number)):
            if player_number[player_symbol] == right_number[right_symbol]:
                if player_symbol == right_symbol:
                    bulls += 1
                else:
                    cows += 1
    print(f'Ваше число: {player_number}, быки: {bulls}, коровы: {cows}')
    player_number = input('Попробуйте еще раз: ')
