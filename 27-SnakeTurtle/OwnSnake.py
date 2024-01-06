import turtle
import time
import random

delay = 0.1
s = turtle.Screen()
s.bgcolor("gray")
s.setup(650,650)
s.tracer(0)
s.title("Snake")
x1 = -315
x2 = 315
y1 = -315
y2 = 315

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.setpos(100,280)


food = turtle.Turtle()
food.penup()
food.speed(0)
food.setpos(0, 100)
food.shape("square")
food.color("red")

snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.direction = "up"
snake.penup()
snake.score = 0

body = []
def up():
    if (snake.direction != "down"):
        snake.direction = "up"
def down():
    if (snake.direction != "up"):
        snake.direction = "down"

def right():
    if (snake.direction != "left"):
        snake.direction = "right"

def left():
    if (snake.direction != "right"):
        snake.direction = "left"

def move():
    xcor = snake.xcor()
    ycor = snake.ycor()
    
    if (snake.direction == "up"):
        snake.sety(ycor + 20)
    if (snake.direction == "down"):
        snake.sety(ycor - 20)
    if (snake.direction == "left"):
        snake.setx(xcor - 20)
    if (snake.direction == "right"):
        snake.setx(xcor + 20)        

s.listen()
s.onkeypress(up, "Up")
s.onkeypress(down, "Down")
s.onkeypress(right, "Right")
s.onkeypress(left, "Left")

def checkFood():
    if (snake.distance(food) < 20):
        xr = random.randint(x1, x2);
        yr = random.randint(y1, y2);
        snake.score += 10
        food.setpos(xr, yr)

        part = turtle.Turtle()
        part.penup()
        part.color("green")
        part.shape("square")
        body.append(part)
        text.clear()
        text.write(snake.score, align = "center", font = ("roboto", 24, "normal"))

    total = len(body)

    for i in range (total -1 , 0 , -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].setpos(x, y)

    if (total > 0):  
        x = snake.xcor()
        y = snake.ycor()  
        body[0].setpos(x , y)
    

while True:
    s.update()    
    checkFood()
    move()
    time.sleep(delay)

turtle.done()