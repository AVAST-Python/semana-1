import turtle

t = turtle.Turtle('turtle')
t.screen.setup(width=1000, height=1000, startx=0, starty=0)

t.speed(100)
t.width(1)
t.penup()
t.goto(-300, 0)
t.pendown()

t.color('red')

# Cuadrado
# for vuelta in range(4):
#     t.forward(100)
#     t.left(90)

# Escalera
# for vuelta in range(4):
#     t.left(90)
#     t.forward(100)
#     t.right(90)
#     t.forward(100)

# Pinchos
# for vuelta in range(4):
#     t.left(90)
#     t.forward(100)
#     t.left(180)
#     t.forward(100)
#     t.left(90)
#     t.forward(100)

# Pinchos extended
# Hacer de al menos 2 formas diferentes
# t.forward(100)
# for vuelta in range(4):
#     t.left(90)
#     t.forward(100)
#     t.left(180)
#     t.forward(100)
#     t.left(90)
#     t.forward(100)


# AQUI, CONTAR ALGO DE EXPRESIONES Y VARIABLES



# Pinchos increasing
# for vuelta in range(7):
#     t.left(90)
#     t.forward(30*vuelta)
#     t.left(180)
#     t.forward(30*vuelta)
#     t.left(90)
#     t.forward(30*vuelta)


# DOBLES BUCLES

# Ejemplo: dos triángulos
for vuelta in range(2):
    for lado in range(3):
        t.forward(100)
        t.left(120)
    t.forward(100)

# Triángulo con cuadrados
# t.right(15)
# for i in range(3):
#     for j in range(4):
#         t.forward(100)
#         t.left(90)
#     t.left(120)

# Ejercicio: triangulos
# for vuelta in range(4):
#     for lado in range(3):
#         t.forward(30+30*vuelta)
#         t.left(120)



# turtle.done()
# t.hideturtle()
turtle.exitonclick()
