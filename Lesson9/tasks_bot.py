tasks = []

task = input('введите задание, которое вам нужно выполнить. Для завершения ввода введите 0 \n')
while task != '0':
    tasks.append(task)
    task = input('введите задание, которое вам нужно выполнить. Для завершения ввода введите 0 \n')

for task in tasks:
    print(task)

while len(tasks) > 0:
    task_completed = input('Какое задание вы выполнили?\n')
    if task_completed not in tasks:
        print('Такого задания не было! Попробуйте еще раз!')
    tasks.remove(task_completed)
    print('осталось выполнить: ')
    
    for task in tasks:
        print(task)

print('Поздравляю, все дела выполнены!')
