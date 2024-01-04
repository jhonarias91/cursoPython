import turtle
import time
from turtle import listen
from turtle import onkey
from turtle import up

delay = 0.1

s = turtle.Screen()
snake = turtle.Turtle()

s.bgcolor("gray")
s.setup(650, 650)
s.title("Snake")

snake.penup()
snake.color("green")
snake.goto(0,0)
snake.shape("square")
snake.speed(1)
snake.direction = "left"

s.listen() #Listen keboard and mouse

def up():
    snake.direction = "up"
def down():
    snake.direction = "down"
def left():
    snake.direction = "left"
def right():
    snake.direction = "right"        

s.onkeypress(up, "Up")
s.onkeypress(down, "Down")
s.onkeypress(left, "Left")
s.onkeypress(right, "Right")

def move ():
    if (snake.direction == 'up'):
        y = snake.ycor()
        snake.sety(y + 20)
    if (snake.direction == 'down'):
        y = snake.ycor()
        snake.sety(y - 20)
    if (snake.direction == 'left'):
        x = snake.xcor()
        snake.setx(x - 20)
    if (snake.direction == 'right'):
        x = snake.xcor()
        snake.setx(x + 20)



while True:
    snake._update()
    move()
    time.sleep(delay)

turtle.done()
