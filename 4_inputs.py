import turtle
import sys

# Personalización de la ventana
window = turtle.Screen()
window.title("Aproximación a un videojuego")
window.bgcolor("skyblue")
window.setup(500, 500)

class Tortuga(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pensize(2)
        self.shape("turtle")
        self.color("darkgreen")

    def mover(self):
        orden = turtle.textinput(
            "Orden de movimiento",
            "Movimientos: A W S D"
        )

        if orden:
            orden = orden.lower()
            if orden == "d":
                self.setheading(0)
            elif orden == "w":
                self.setheading(90)
            elif orden == "a":
                self.setheading(180)
            elif orden == "s":
                self.setheading(270)
        else:
            sys.exit()

        self.forward(100)


kame = Tortuga()

while 1:
    kame.mover()