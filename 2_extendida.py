import turtle
import math

# Personalización de la ventana
window = turtle.Screen()
window.title("Dibujando con una tortuga")
window.bgcolor("skyblue")
window.setup(500, 500)
window.setworldcoordinates(0, 500, 500, 0) # Interpreta ESTA coordenada como la fija

class Tortuga(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pensize(2)
        self.shape("turtle")
        self.color("darkgreen")

    def rectangulo(self, x, y, ancho, alto, color="black"):
        self.color(color)
        self.penup()
        self.goto(x-ancho/2, y-alto/2) # vértice sup izq
        self.pendown()
        self.goto(x+ancho/2, y-alto/2) # vértice sup der
        self.goto(x+ancho/2, y+alto/2) # vértice inf der
        self.goto(x-ancho/2, y+alto/2) # vértice inf izq
        self.goto(x-ancho/2, y-alto/2) # vértice sup izq
    
    def poligono(self, lados, radio, color="white"):
        self.color(color)
        angulo = math.pi * 2 / lados
        ancho_ventana = window.screensize()[0]/2
        alto_ventana = window.screensize()[1]/2
        x = radio * math.sin(angulo) + ancho_ventana
        y = radio * math.cos(angulo) + alto_ventana
        self.penup()
        self.goto(x, y)
        self.pendown()
        for i in range(lados+1):
            x = radio * math.sin(angulo*i) + ancho_ventana
            y = radio * math.cos(angulo*i) + alto_ventana
            self.goto(x, y)


kame = Tortuga()

angulo = math.pi * 2
ancho_ventana = window.screensize()[0]/2
alto_ventana = window.screensize()[1]/2
x = math.sin(angulo) + ancho_ventana
y = math.cos(angulo) + alto_ventana
"""x, y = (250, 250)"""
w, h = (50, 50)
inc = 50

for color in ["yellow", "orange", "red", "brown", "purple", "blue", "cyan", "green", "black"]:
    kame.rectangulo(x,y,w,h, color=color)
    w += inc
    h += inc

for n in range(4, 25):
    kame.poligono(n, n*10)
    kame.speed(8)

turtle.mainloop()