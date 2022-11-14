import turtle
import time
import random




# set up the screen
wn=turtle.Screen()
wn.title("Star Fleet")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#decorator
dec = turtle.Turtle()
dec.speed(0)
dec.hideturtle()
dec.penup()
dec.color("white")
dec.goto(300,300)
dec.pendown()
dec.goto(-300,300)
dec.goto(-300,-300)
dec.goto(300,-300)
dec.goto(300,300)
for i in range(20):
    dec.penup()
    dec.goto(random.randint(-300,300),random.randint(-300,300))
    dec.pendown()
    dec.circle(random.randint(1,3))
dec.penup()
dec.goto(600,600)



# main character
m_c = turtle.Turtle()
m_c.speed(0)
m_c.shape("turtle")
m_c.shapesize(1, 2, 0)
m_c.color("white")
m_c.penup()
m_c.goto(0,0)
m_c.direction = "stop"

# killer
klr = turtle.Turtle()
klr.hideturtle()
klr.speed(1)
klr.shape("arrow")
klr.shapesize(3)
klr.color("red")
klr.penup()
klr.goto(610,610)


# collect
coin=turtle.Turtle()
coin.speed(0)
coin.shape("circle")
coin.color("yellow")
coin.penup()
coin.goto(0,100)


score = 0
high_score = 0
delay = 0.1
x = 0
y = 0

# Score pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Счет: {score}  Рекорд: {high_score}", align = "center", font = ("Courier", 24, "normal"))


def move_up():
    m_c.direction = "up"
    m_c.setheading(90)

def move_down():
    m_c.direction = "down"
    m_c.setheading(270)
def move_left():
    m_c.direction = "left"
    m_c.setheading(180)

def move_right():
    m_c.direction = "right"
    m_c.setheading(0)

def m_check():
    if m_c.direction == "up":
        y = m_c.ycor()
        m_c.sety(y+20)
    if m_c.direction == "down":
        y = m_c.ycor()
        m_c.sety(y-20)
    if m_c.direction == "left":
        x = m_c.xcor()
        m_c.setx(x-20)
    if m_c.direction == "right":
        x = m_c.xcor()
        m_c.setx(x+20)


    
wn.listen()
# keyboard bindings
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")



while True:
    wn.update()
    
    
        # Check for a collision with the border
    if m_c.xcor()>300 or m_c.xcor()<-300 or m_c.ycor()>300 or m_c.ycor()<-300:
        time.sleep(1)
        m_c.direction = "stop"
        m_c.goto(0,0)
        klr.goto(610,610)
           
        # Reset the score        
        score=0        
        pen.clear()
        pen.write(f"Счет: {score}  Рекорд: {high_score}", align="center", font=("Courier", 24, "normal"))

    m_check()

    #Check for a collision with the coin
    if m_c.distance(coin) < 20:
        # move the coin to a random spot
        x=random.randint(-250,250)
        y=random.randint(-250,250)
        coin.goto(x,y)
        # Increase the score      
        score+=10

        if score > high_score:
           
            high_score = score
        pen.clear()
        pen.write(f"Счет: {score}  Рекорд: {high_score}",align="center",font=("Courier", 24, "normal"))

    if score >= 50:
        klr.showturtle()
        klr.setheading(klr.towards(m_c.xcor(),m_c.ycor()))
        if score >= 50 and score < 100:
            klr.fd(5)
        elif score >= 100:
            klr.fd(10)
        
        if klr.distance(m_c) < 25:
            time.sleep(1)
            m_c.direction = "stop"
            m_c.goto(0,0)
            klr.goto(610,610)
           
            #  Reset the score        
            score=0        
            pen.clear()
            pen.write(f"Счет: {score}  Рекорд: {high_score}", align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)
        

    
        
wn.mainloop()