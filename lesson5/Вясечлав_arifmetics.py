from random import *
import time
import os

def newprint(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

os.system('clear')


newprint('\n \nТренажёр по Арифметике')
time.sleep(1)
newprint('\n1 - Начать')
start = input()

if start == '1':
    newprint('\nВыбирите уровень сложности')
    newprint('\n 1 -Легко \n2 - Нормально \n3 - Сложно')
    hard = input()





if hard == '1':
        time.sleep(1)

        operation = (input("Какое действие вы хотите делать? ( +, -, /, *,)   "))
        time.sleep(1)
        quantity = int(input("Сколько примеров вы хотите решить? "))




        if operation == '/':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(10,15)
                b =randint(1,10)
                c =round(a/b, 1)
                print('\nСколько будет', a, "/", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 80:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 60:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 40:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3) 



        if operation == '+':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(1,30)
                b =randint(1,30)
                c =round(a+b, 1)
                print('\nСколько будет', a, "+", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 80:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 60:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 40:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3)  


                    
        if operation == '-':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(20,50)
                b =randint(1,20)
                c =round(a-b, 1)
                print('\nСколько будет', a, "-", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 80:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 60:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 40:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3)  



        if operation == '*':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(1,10)
                b =randint(1,10)
                c =round(a*b, 1)
                print('\nСколько будет', a, "*", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 90:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 70:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 50:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3)  





if hard == '2':
        time.sleep(1)

        operation = (input("Какое действие вы хотите делать? ( +, -, /, *,)   "))
        quantity = int(input("Сколько примеров вы хотите решить? "))

        if operation == '/':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(20,80)
                b =randint(1,20)
                c =round(a/b, 1)
                print('\nСколько будет', a, "/", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 80:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 60:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 40:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3)  



        if operation == '+':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(10,100)
                b =randint(10,100)
                c =round(a+b, 1)
                print('\nСколько будет', a, "+", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 80:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 60:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 40:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3)  


                    
        if operation == '-':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(50,100)
                b =randint(1,50)
                c =round(a-b, 1)
                print('\nСколько будет', a, "-", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 80:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 60:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 40:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3)  



        if operation == '*':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(1,30)
                b =randint(1,30)
                c =round(a*b, 1)
                print('\nСколько будет', a, "*", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 90:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 70:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 50:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3)  




if hard == '3':
        time.sleep(1)

        operation = (input("Какое действие вы хотите делать? ( +, -, /, *,)    "))
        quantity = int(input("Сколько примеров вы хотите решить?    "))

        if operation == '/':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(25,250)
                b =randint(10,50)
                c =round(a/b, 1)
                print('\nСколько будет', a, "/", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 80:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 60:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 40:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3)  



        if operation == '+':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(150,3500)
                b =randint(150,3500)
                c =round(a+b, 1)
                print('\nСколько будет', a, "+", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 80:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 60:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 40:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3)  


                    
        if operation == '-':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(25,2500)
                b =randint(25,2500)
                c =round(a-b, 1)
                print('\nСколько будет', a, "-", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 80:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 60:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 40:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3)  



        if operation == '*':
            correct = 0
            incorrect = 0
            for x in range (quantity):
                a =randint(10,200)
                b =randint(10,200)
                c =round(a*b, 1)
                print('\nСколько будет', a, "*", b)
                answer =eval(input("Напиши ответ:  "))
                if answer == c:
                    newprint('\nПравильно')
                    correct = correct + 1

                if answer != c:
                    print('\nНе правильно,', 'Правильный ответ', c)
                    incorrect = incorrect + 1

            time.sleep(1.5)
            print('У тебя', correct, 'Правильных и', incorrect, 'неправильных ответов')
            percent = correct/quantity*100
            if percent >= 90:
                time.sleep(0.5)
                newprint('У тебя все прекрасно с арифметикой!')
            elif percent >= 90:
                time.sleep(0.5)
                newprint('Ты справился хорошо ,но есть над чем поработать')
            elif percent >= 70:
                time.sleep(0.5)
                newprint('У тебя нормальный уровень ,но есть много над чем поработать')
            elif percent >= 50:
                time.sleep(0.5)
                newprint('У тебя не очень хорошо ,но нужно работать')
            else:
                time.sleep(0.5)
                newprint('У тебя все плохо ,но не растраивайся ,а продолжай тренироваться')
                time.sleep(3)  
