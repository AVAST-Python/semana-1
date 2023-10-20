import turtle
from configure_screen import position_screen

# Turtle script example
t = turtle.Turtle('turtle')
position_screen(t)

t.speed(100)

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
t.penup()
t.setpos(-200,-300)
t.setheading(0)
t.pendown()

import math
base = 100
angulo = 75

altura = ( base / 2 ) * math.tan(math.radians(angulo))
lado = math.sqrt(  ( base / 2 )**2 + altura**2   )

print(altura)
print(lado)


t.forward(base)
t.left(180-angulo)
t.forward(lado)
t.left(2*angulo)
t.forward(lado)

t.penup()
t.forward(100)

t.hideturtle()
turtle.exitonclick()
