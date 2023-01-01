import turtle

# Personalización de la ventana
window = turtle.Screen()
window.title("Pruebas con turtle")
window.bgcolor("skyblue")
window.setup(500, 500)
window.setworldcoordinates(0, 500, 500, 0) # Interpreta ESTA coordenada como la fija

# Personalización de la tortuga
kame = turtle.Turtle()
kame.shape("turtle")
kame.color("darkgreen")
kame.pensize(2)
kame.speed(2)

# Instrucciones de la tortuga
for i in range(0, 6):
    kame.penup()
    kame.goto(i*25, i*25)
    kame.pendown()
    kame.circle(i*25)
    
turtle.mainloop()
