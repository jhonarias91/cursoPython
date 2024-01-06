import turtle
import random

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Tetris by Jhon")
wn.bgcolor("black")
wn.setup(width=600, height=800)

# Creación de la "tortuga" para dibujar
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

# Definición de las piezas
shapes = [
    [[1, 1, 1, 1]], # Línea
    [[1, 1], [1, 1]], # Cuadrado
    [[0, 1, 0], [1, 1, 1]], # T
    [[1, 0, 0], [1, 1, 1]], # L
    [[0, 0, 1], [1, 1, 1]], # J
    [[1, 1, 0], [0, 1, 1]], # S
    [[0, 1, 1], [1, 1, 0]]  # Z
]

# Función para dibujar piezas
def draw_piece(piece, x, y):
    for y_offset, row in enumerate(piece):
        for x_offset, cell in enumerate(row):
            if cell:
                draw_square(x + x_offset, y - y_offset)

# Función para dibujar un cuadrado (parte de una pieza)
def draw_square(x, y):
    pen.goto(x*20, y*20)
    pen.stamp()

# Prueba de dibujo
piece = random.choice(shapes)
draw_piece(piece, 0, 0)

wn.mainloop()
