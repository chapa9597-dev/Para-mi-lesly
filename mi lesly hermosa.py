# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 16:34:23 2025

@author: chapa
"""

import turtle
import time

# Configurar pantalla
pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("Mensaje Especial")
pantalla.tracer(0)  # Desactiva actualización automática

# Crear tortuga para la flor
flor = turtle.Turtle()
flor.hideturtle()
flor.speed(0)

# Crear tortugas para el texto (una arriba y una abajo)
texto_arriba = turtle.Turtle()
texto_abajo = turtle.Turtle()

for t in (texto_arriba, texto_abajo):
    t.hideturtle()
    t.color("white")
    t.penup()

# Crear tortuga para el corazón
corazon = turtle.Turtle()
corazon.hideturtle()
corazon.speed(0)
corazon.color("red")
corazon.penup()

# Crear tortuga para el texto dentro del corazón
texto_corazon = turtle.Turtle()
texto_corazon.hideturtle()
texto_corazon.color("white")
texto_corazon.penup()

# Función para dibujar una capa de pétalos
def dibujar_capa(tortuga, petalos, radio, color, grosor):
    tortuga.color(color)
    tortuga.fillcolor(color)
    tortuga.pensize(grosor)
    for _ in range(petalos):
        tortuga.begin_fill()
        tortuga.circle(radio, 60)
        tortuga.left(120)
        tortuga.circle(radio, 60)
        tortuga.left(120)
        tortuga.end_fill()
        tortuga.right(360 / petalos)

# Dibujar la flor y hacerla girar
def dibujar_flor():
    flor.clear()
    flor.penup()
    flor.goto(0, 0)
    flor.setheading(flor.heading() + 2)
    flor.pendown()
    dibujar_capa(flor, 12, 120, "#C71585", 2)
    dibujar_capa(flor, 12, 90, "pink", 2)
    dibujar_capa(flor, 12, 60, "yellow", 2)

# Escribir texto con animación de letra por letra (no borrar)
def escribir_texto_animado(tortuga, texto, posicion, fuente=("Courier", 14), delay=0.05):
    tortuga.goto(posicion)
    x, y = posicion
    linea = ""
    for letra in texto:
        if letra == "\n":
            tortuga.goto(x, y)
            tortuga.write(linea, align="center", font=fuente)
            linea = ""
            y -= 25
            tortuga.goto(x, y)
        else:
            linea += letra
        pantalla.update()
        time.sleep(delay)
    # Escribe la última línea
    tortuga.goto(x, y)
    tortuga.write(linea, align="center", font=fuente)
    pantalla.update()

# Función para dibujar un corazón escalado en (0,0)
def dibujar_corazon(tortuga, escala=1.0):
    tortuga.clear()
    tortuga.penup()
    tortuga.goto(0, -100 * escala)
    tortuga.pendown()
    tortuga.fillcolor("red")
    tortuga.begin_fill()
    tortuga.setheading(140)
    tortuga.forward(112 * escala)
    for _ in range(200):
        tortuga.right(1)
        tortuga.forward((1.12 * escala))
    tortuga.setheading(60)
    for _ in range(200):
        tortuga.right(1)
        tortuga.forward((1.12 * escala))
    tortuga.forward(112 * escala)
    tortuga.end_fill()

# Función para animar el corazón latiendo con texto "Te amo"
def animar_corazon(latidos=6, delay=0.15):
    for i in range(latidos):
        # Crecer
        dibujar_corazon(corazon, escala=1.1)
        texto_corazon.clear()
        texto_corazon.goto(0, -20)
        texto_corazon.write("Te amo", align="center", font=("Courier", int(24*1.1), "bold"))
        pantalla.update()
        time.sleep(delay)
        # Encoger
        dibujar_corazon(corazon, escala=0.9)
        texto_corazon.clear()
        texto_corazon.goto(0, -20)
        texto_corazon.write("Te amo", align="center", font=("Courier", int(24*0.9), "bold"))
        pantalla.update()
        time.sleep(delay)
    # Dejar tamaño normal
    dibujar_corazon(corazon, escala=1.0)
    texto_corazon.clear()
    texto_corazon.goto(0, -20)
    texto_corazon.write("Te amo Lesly", align="center", font=("Courier", 24, "bold"))
    pantalla.update()

# Animación principal
def animar():
    mensaje_arriba = (
        "De verdad no quiero dejarte\n"
        "no quiero alejarme de la mujer que me hizo feliz y amar\n"
        "Eres mi motivo de ser feliz"
    )
    mensaje_abajo = (
        "Quiero ser lo mismo que éramos antes\n"
        "No puedo estar sin ti\n"
        "¿Quieres regresar conmigo?"
    )

    # Flor gira al inicio
    for _ in range(50):
        dibujar_flor()
        pantalla.update()
        time.sleep(0.05)

    # Escribir el texto de arriba (queda fijo)
    escribir_texto_animado(texto_arriba, mensaje_arriba, (0, 260), ("Courier", 14, "bold"), 0.05)

    for _ in range(50):
        dibujar_flor()
        pantalla.update()
        time.sleep(0.05)

    # Escribir el texto de abajo (queda fijo)
    escribir_texto_animado(texto_abajo, mensaje_abajo, (0, -260), ("Courier", 14, "italic"), 0.05)

    # Seguir girando un poco más
    for _ in range(30):
        dibujar_flor()
        pantalla.update()
        time.sleep(0.05)

    # Limpiar la pantalla para mostrar el corazón latiendo
    flor.clear()
    texto_arriba.clear()
    texto_abajo.clear()

    # Animar corazón latiendo
    animar_corazon(latidos=8, delay=0.2)

# Ejecutar animación
animar()
turtle.done()
