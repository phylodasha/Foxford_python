def print_rules():
    print("Правила игры:")
    print("* Ведущий задает вопрос")
    print("* У игрока 3 попытки правильно ответить на него")
    print("* Ответ вводится маленькими буквами")

def ask_question(question, right_answer, count_try):
    print(question)
    player_number = input("Ваш ответ: ")
    count_try = count_try - 1
    while player_number != right_answer and count_try > 0:
        print("Попробуй еще раз!")
        print(f"Количество потраченных попыток: {3 - count_try}")

        player_number = input("Ваш ответ: ")
        count_try = count_try - 1

    if player_number == right_answer:
        print("Поздравляю с победой!")
        print(f"Количество потраченных попыток: {3 - count_try}")
    else:
        print("Не повезло! Но в следующий раз обязательно повезет!")

def game(question_list, answer_list, count_try):
    print_rules()
    for i in range(len(question_list)):
        ask_question(question_list[i], answer_list[i], count_try)
    print('Поздравляем с завершением викторины!')



question_list = [
    "В каком году открыли первую в России станцию метро?",
    "Сколько дней в ноябре?",
    "Когда просыпается хомяк?",
    "Когда открылся Эрмитаж?"
]

answer_list = [
    "1935",
    "30",
    "Ночью",
    "1764"
]


game(question_list, answer_list, 3)