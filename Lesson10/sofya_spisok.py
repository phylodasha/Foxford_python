import time
def newprint(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.05)
tasks = list()

newprint('Привет! Я бот, который будет помогать вам с выполнением разных дел\n')
newprint('Я могу хранить дела в списке и вычеркивать их, когда вы их выполните\n')
newprint('Вводите дела отдельными сообщениями, а когда захотите закончить формироание списка дел, то введите 0\n')
task = input('Введите дело: ')

while task != '0':
    tasks.append(task)
    task = input('Введите дело: ')

iterator = 0
while iterator < len(tasks):
    newprint(f'{iterator+1}. {tasks[iterator]}')
    iterator += 1

while len(tasks)>0:
    user_input = input('Какое дело вы завершили? ')
    tasks.remove(user_input)
    iterator=0
    while iterator < len(tasks):
        print(f'{iterator+1}. {tasks[iterator]}')
        iterator += 1

newprint('Все дела завершены! Можете отдыхать')
pass