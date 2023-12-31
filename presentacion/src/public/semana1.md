

# Introducción a Python

![alt text](./img/logo2.png) <!-- .element style="margin-left: auto; margin-right: auto; display: block" -->

Notes:
Pasar la [encuesta](https://forms.gle/62m79xAeYoMCi8WV8)

---

![alt text](./img/jim-carrey-jim-carrey-typing.gif) <!-- .element style="margin-left: auto; margin-right: auto; display: block" -->

---

# Tenemos un plan

![Tenemos un plan](./img/tenemos_un_plan.jpg) <!-- .element class="medium right" -->

### Parte I: programación
- Python básico
- Algoritmos
- Herramientas de programación (git, tests, etc.)
- Proyecto final: juego
- Proyecto extra: bot de Telegram

### Parte II: Inteligencia Artificial
- Introducción a la IA
- Modelos con Tensorflow / Pytorch
- Proyecto final: reconocimiento de fotografías


---


### La programación son cinco cosas

1. Secuencia
2. Condicionales
3. Repetición
4. Variables
5. Funciones


---

# ¡A pintá!


![Una casita](./img/casita.png) <!-- .element class="big center" -->

--

[https://pythonandturtle.com/turtle](https://pythonandturtle.com/turtle)

### Estructura básica de código


```python [0|1-2|4-14|16]
# Turtle script example
t = turtle.Turtle('turtle')

t.width(1)
t.speed (1)
t.color('red')

t.forward(50)

for i in range(4):
  t.forward(100)
  t.left(90)

t.backward(50)

turtle.done()
```

- Inicialización (siempre igual)
- Hacer cosas
- Terminar (siempre igual)


--

### Mover la tortuga

- Velocidad

```python
t.speed(1) # 1 lento, 500 rápido
```

- Avanzar / Retroceder:

```python
t.forward(50)
t.backward(50)

t.forward(-50)
t.backward(-50)
```

- Girar. En º y admite negativos:


```python
t.left(90)
t.right(45)
```

- Control del lápiz

```python
t.penup()
t.pendown()
t.color('red')
```

--

# Pues a pintá

[https://pythonandturtle.com/turtle](https://pythonandturtle.com/turtle)
<!-- .element class="centered" style="margin-top: -3rem;" -->

**OJO**: las mayúsculas/minúsculas son importantes
<!-- .element class="centered" -->

**OJO**: la alineación del código es importante
<!-- .element class="centered" -->

![Ejercicio 1](./img/ejercicio_1.png) <!-- .element class="noborder center" -->

- *Extra*: Dibuja un triángulo isósceles
- *Super extra*: Dibuja un triángulo isósceles... y no lo hagas "a ojo"

Note:
- Ejemplo: cuadrado
https://docs.python.org/3/library/turtle.html#turtle-graphics-reference

---

# A almorzá

- Presentación: [https://avast-python.github.io/semana-1/](https://avast-python.github.io/semana-1/)
- Soluciones: [https://github1s.com/AVAST-Python/semana-1](https://github1s.com/AVAST-Python/semana-1)


