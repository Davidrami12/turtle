import turtle
import sys

# Personalización de la ventana
window = turtle.Screen()
window.title("Videojuego de una tortuga")
window.bgcolor("skyblue")
window.setup(500, 500)

class Tortuga(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pensize(2)
        self.shape("turtle")
        self.color("darkgreen")

    def adelante(self):
        self.forward(10)

    def atras(self):
        self.backward(10)

    def derecha(self):
        self.right(10)

    def izquierda(self):
        self.left(10)


    
kame = Tortuga()
window.onkey(kame.adelante, "w")
window.onkey(kame.derecha, "d")
window.onkey(kame.atras, "s")
window.onkey(kame.izquierda, "a")
window.onkey(sys.exit, "e")
window.listen()
turtle.mainloop()