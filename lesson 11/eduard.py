from tkinter import *                  
from tkinter.dialog import *                   
from random import choice                       
from time import *                          
x = ''                                          
n = 0                                        
t = 0                                          

def play(event):                             
    '''
    Функция которая получает число из поля ввода от игрока,
    сравнивает каждую цифру введённую игроком с загаданным числом x,
    и выводит результаты в окно сообщений msg.
    '''
    global x, n, t                            
    if len(x) == 0:                             
        z = '0123456789'                        
        x = choice(z[1:10])                    
        for i in range(3):                
            z = ''.join(z.split(x[i]))        
            x += choice(z)                    
        msg2.config(text='')                    
        t = time()                              
    y = ent.get()                              
    b = 0; c = 0                               
    for i in range(4):                          
        if x[i] == y[i]:                        
            b += 1                          
        elif y[i] in x:                         
            c += 1                              
    n += 1                                         
    msg2.config(text = msg2.cget('text') + str(n) + '. Ваше число: ' + y + ' содержит ' + str(b) + ' быка и ' + str(c) + ' коровы\n')
    ent.delete(0, END)                        
    if b == 4:                                
        gameOwer = Dialog(title = 'Вы победили за ' + str(n) + ' ходов; ' + str(int(time()-t)) + ' сек.',
               text = '     Сыграем ещё?           ',
               bitmap = 'questhead',
               default = 0,
               strings = ('Да', 'Нет'))
        if gameOwer.num == 1: exit()           
        n = 0                              
        x = ''                                  
        msg2.config(text='Бык - цифра на своём месте.\n'
               'Корова - цифра не на своём месте.')    

tk = Tk()                                       
tk.geometry('500x350')                        
tk.title('Быки и Коровы')                       

msg = Message(width=400, padx=10, pady=5,
              text='Введите следующее число от 1023 до 9876 '
              'такое, чтобы цифры, составляющие это число,'
              ' не повторялись!')              
msg.pack(padx=10, pady=5)                       
msg.config(bg='light grey', fg='olive',
           font=('times', 12, 'italic'))        

ent = Entry(width=4)                         
ent.pack()                                      
ent.bind( '<Return>', play)                    
                                               

msg2 = Message(width=400, padx=10, pady=5,
              text='Бык - цифра на своём месте.\n'
               'Корова - цифра не на своём месте.')    
msg2.pack(padx=10, pady=5)                    
msg2.config(font=('times', 12, 'normal'))       

mainloop() 