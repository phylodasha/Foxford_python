tasks = []

task = input('введите задание, которое вам нужно выполнить. Для завершения ввода введите 0 \n')
while task != '0':
    tasks.append(task)
    task = input('введите задание, которое вам нужно выполнить. Для завершения ввода введите 0 \n')

i = 0
while i < len(tasks):
    print(f'{i + 1} - {tasks[i]}')
    i += 1

while len(tasks) > 0:
    task_completed = input('Какое задание вы выполнили?\n')
    tasks.remove(task_completed)
    print('осталось выполнить: ')
    i = 0
    while i < len(tasks):
        print(f'{i + 1} - {tasks[i]}')
        i += 1

print('Поздравляю, все дела выполнены!')
