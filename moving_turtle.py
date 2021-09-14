import turtle

def press_w():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def press_s():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def press_a():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def press_d():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(press_w, 'w')
turtle.onkey(press_s, 's')
turtle.onkey(press_a, 'a')
turtle.onkey(press_d, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
