import turtle

t = turtle.Turtle('turtle')
t.screen.setup(width=1000, height=1000, startx=0, starty=0)

t.width(4)
t.speed (500)
t.color('#4689BC')

t.penup()
t.goto(-450, 100)
t.pendown()

# DOBLES BUCLES

# Ejemplo: dos triángulos
# for vuelta in range(2):
#     for lado in range(3):
#         t.forward(100)
#         t.left(120)
#     t.forward(100)

# Triángulo con cuadrados
# t.right(15)
# for i in range(3):
#     for j in range(4):
#         t.forward(100)
#         t.left(90)
#     t.left(120)

# Estrella
# Pista: En un polígono regular todos los ángulos internos son iguales
# y la suma es igual a 180° × (n – 2).
lados = 3
angulo_interno = 180 * (lados - 2) / lados
angulo_giro = 180 - angulo_interno

# for vuelta in range(lados):
#     t.forward(100)
#     t.left(angulo_giro)

# Triangulos inscritos
# for vuelta in range(4):
#     for lado in range(3):
#         t.forward(30+30*vuelta)
#         t.left(120)



t.hideturtle()
turtle.exitonclick()
