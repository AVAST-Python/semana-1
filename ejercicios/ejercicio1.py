import turtle

# Turtle script example
t = turtle.Turtle('turtle')

t.speed(100)
# t.screen.setup (width=1024, height=1024, startx=3020, starty=200) # Right monitor
t.screen.setup (width=1024, height=900, startx=500, starty=0) # Left monitor

t.penup()
t.setpos(-500, 000)
t.pendown()

t.width(1)
t.speed (500)
t.color('red')

# Cuadrado
# TO-DO

# Escalera
t.lt(90)
t.fd(100)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(50)
t.lt(90)
t.fd(150)
t.rt(90)
t.fd(50)

# Triangulo equilátero


# Triángulo isósceles
# Hint: cos(60) = 1/2



# turtle.done()
# t.hideturtle()
turtle.exitonclick()
