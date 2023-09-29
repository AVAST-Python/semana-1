import turtle

# Turtle script example
t = turtle.Turtle('turtle')

t.speed(100)
# t.screen.setup (width=1024, height=1024, startx=3020, starty=200) # Right monitor
t.screen.setup (width=1024, height=900, startx=500, starty=0) # Left monitor

t.penup()
t.setpos(-500, 000)
t.pendown()

t.width(4)
t.speed (500)
t.color('#4689BC')

# Ejemplo: cuadrado
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.penup()
t.left(90)
t.forward(200)
t.pendown()

# Escalera
t.left(90)
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(50)
t.left(90)
t.forward(150)
t.right(90)
t.forward(50)


t.penup()
t.left(90)
t.forward(100)
t.pendown()


# Triangulo equilátero
t.forward(100)
t.left(180-60)
t.forward(100)
t.left(180-60)
t.forward(100)


t.penup()
t.left(180-60)
t.forward(200)
t.pendown()

# Casita
# Habitaciones
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
# Techo
t.left(90)
t.forward(100)
t.right(90-60)
t.forward(100)
t.right(180-60)
t.forward(100)

# Triángulo isósceles
# t.penup()
# t.setpos(-200,0)
# t.pendown()




# import math
# top_angle = 40
# base_angle = (180 - top_angle) / 2
# base = 100
# altura = base/2 *math.sin(base_angle)


# t.color('blue')
# t.forward(base/2)
# t.left(90)
# t.forward(altura)
# t.penup()
# t.setpos(-200,0)
# t.pendown()
# t.setheading(0)
# t.color('red')

# side = math.sqrt((base/2)**2 + altura**2)

# t.forward(base)
# t.left(180-base_angle)
# t.forward(side)
# t.left(180-top_angle)
# t.forward(side)
# t.left(180-base_angle)

t.hideturtle()
turtle.exitonclick()
