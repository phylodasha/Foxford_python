from secrets import choice

wanting = input("Здравствуйте! Хотите ли Вы сыграть в игру «FunnyProverbGame»? ").lower()
if wanting == "да":
    print(f"\nПравила игры «FunnyProverbGame» просты:\nВспомните 5 пословиц, каждую из которых разделите на две половины\nВставляйте по половине, когда система будет просить их ввести.")
    halfof1 = input("\nВведите первую половину первой пословицы: ")
    secondhalfof1 = input("Введите вторую половину первой пословицы: ")
    halfof2 = input("Введите первую половину второй пословицы: ")
    secondhalfof2 = input("Введите вторую половину второй пословицы: ")
    halfof3 = input("Введите первую половину третьей пословицы: ")
    secondhalfof3 = input("Введите вторую половину третьей пословицы: ")
    halfof4 = input("Введите первую половину четвёртой пословицы: ")
    secondhalfof4 = input("Введите вторую половину четвёртой пословицы: ")
    halfof5 = input("Введите первую половину пятой пословицы: ")
    secondhalfof5 = input("Введите вторую половину пятой пословицы: ")
    Firsthalfs = [halfof1, halfof2, halfof3, halfof4, halfof5]
    Secondhalfs = [secondhalfof1, secondhalfof2, secondhalfof3, secondhalfof4, secondhalfof5]
    while len(Firsthalfs) != 0:
        one = choice(Firsthalfs)
        two = choice(Secondhalfs)
        print(f"\n{one} {two}")
        answer = input("Верно ли составлена пословица? ").lower()
        if answer == "да":
            Firsthalfs.remove(one)
            Secondhalfs.remove(two)
            print("\nУра!")
            print(f"Осталось собрать пословиц: {len(Firsthalfs)}")
        elif answer == "нет":
            print("\nНу ладно...")
            print(f"Осталось собрать пословиц: {len(Firsthalfs)}")
    print("Поздравляю! Все пословицы собраны!")
elif wanting == "нет":
    print("Что-ж... Тогда заходите в другой раз")



