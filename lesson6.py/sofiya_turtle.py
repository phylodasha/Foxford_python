import turtle, time

t = turtle.Turtle()
t.speed(0)
##корпус
#t.pencolor("black")
#t.fillcolor("grey")
t.color("black", "grey")
t.begin_fill()
t.fd(100)
t.left(90)
t.fd(250)
t.left(90)

t.fd(100)
t.left(90)
t.fd(250)
t.left(90)
t.end_fill()


#kabina

t.penup()
t.home()
t.pendown()

t.left(90)
t.forward(250)
t.right(90)

t.color("black", "red")

t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

#krilo_left

t.penup()
t.home()
t.pendown()

t.color("black", "green")

t.begin_fill()
t.left(90)
t.fd(100)

t.left(90)
t.left(40)
t.fd(100)
t.left(50)
t.fd(150)
t.left(130)
t.fd(100)
t.left(50)
t.fd(100)
t.end_fill()

# #krilo_right
t.penup()
t.home()

t.left(90)
t.fd(100)
t.right(90)
t.fd(100)

t.pendown()

t.begin_fill()
t.right(40)
t.fd(100)

t.right(50)
t.fd(150)

t.right(130)
t.fd(100)
t.right(50)
t.fd(150)
t.end_fill()

#illuminati
t.speed(1)
t.penup()
t.home()

t.forward(50)
t.left(90)
t.forward(100)
t.right(90)



t.pendown()
t.color("black", "cyan")

t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()

t.left(90)
t.fd(75)
t.right(90)

t.pendown()

t.begin_fill()
t.circle(25)
t.end_fill()

#razdelitel'
t.penup()
t.home()
t.pendown()
t.color("black", "green")

t.begin_fill()
t.left(90)
t.fd(20)
t.right(90)
t.fd(100)
t.right(90)
t.fd(20)
t.right(90)
t.fd(100)

t.end_fill()


# #ogon'
t.penup()
t.home()
t.fd(5)
t.pendown()

t.color("red", "orange")

t.begin_fill()
t.right(90)
t.fd(100)
t.left(30)
t.fd(30)
t.left(120)
t.fd(30)
t.right(120)
t.fd(30)
t.left(120)
t.fd(30)
t.right(120)
t.fd(30)
t.left(120)
t.fd(30)
t.left(30)
t.fd(100)
t.left(90)
t.fd(95)
t.end_fill()
time.sleep(5)