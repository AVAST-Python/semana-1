

# This is a presentation

Hello, world.

![alt text](banana.jpg) <!-- .element style="margin-left: auto; margin-right: auto; display: block" -->


---


# Tenemos un plan

![Tenemos un plan](tenemos_un_plan.jpg) <!-- .element class="medium right" -->

### Parte I: programación
- Python básico
- Algoritmos
- Proyecto final: juego

### Parte II: IA
- Introducción a la IA
- Modelos con Tensorflow / Pytorch
- Proyecto final: reconocimiento de fotografías


---


### La programación son cuatro cosas

1. Secuencia
2. Condicionales
3. Repetición
4. Funciones

---

# ¡A pintá!


![Una casita](casita.png) <!-- .element class="big center" -->

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



**OJO**: las mayúsculas son importantes
<!-- .element class="centered" -->

**OJO**: la alineación es importante
<!-- .element class="centered" -->

EJERCICIOS SECUENCIA

Note:
https://docs.python.org/3/library/turtle.html#turtle-graphics-reference
