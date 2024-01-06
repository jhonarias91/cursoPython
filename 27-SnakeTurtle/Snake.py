import turtle
import time
import random

delay = 0.08

s = turtle.Screen()

s.bgcolor("gray")
s.setup(650, 650)
s.title("Snake")
s.tracer(0) #turns off the automatic updating of the Turtle graphics 


snake = turtle.Turtle()
snake.speed(1)
snake.penup()
snake.color("green")
snake.goto(0,0)
snake.shape("square")
snake.direction = "up"
snake.score = 0

food = turtle.Turtle()
food.penup()
food.speed()
food.color("orange")
food.shape("circle")
food.goto(0,100)

body = []

text = turtle.Turtle()
text.penup()
text.hideturtle()
text.goto(-10, 280)

def up():
    if snake.direction != "down":
        snake.direction = "up"
def down():
    if snake.direction != "up":
        snake.direction = "down"
def left():
    if snake.direction != "right":
        snake.direction = "left"
def right():
    if snake.direction != "left":
        snake.direction = "right"        

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

s.listen() #Listen keboard and mouse
s.onkeypress(up, "Up") #When press the key Up, call the method up()
s.onkeypress(down, "Down")
s.onkeypress(left, "Left")
s.onkeypress(right, "Right")
def checkColliders():
    xcor = snake.xcor()
    ycor = snake.ycor()

    if (xcor < -325 or xcor > 325):
        over()
    
    if (ycor < -325 or ycor > 325):
        over()

    for i in body:
        if (snake.distance(i) < 20):
            over()

def over():    
    for i in body:
       i.goto(1000,1000)
       i.clear()
    body.clear()
    snake.setpos(0,0)
    snake.direction = 'stop'   
    snake.score = 0  
    text.clear()

while True:
    s.update()
    checkColliders()
    if (snake.distance(food) < 20 ):        
        rx = random.randrange(-310, 310)
        ry = random.randrange(-310, 310)  
        food.hideturtle()
        food.speed(0)
        #food.goto(rx, ry) with this the food is moved pixel by pixel
        food.setpos(rx, ry)
        food.showturtle()
        newBody = turtle.Turtle()        
        newBody.speed(0)
        newBody.penup()       
        newBody.shape("square")
        newBody.color("green")        
        body.append(newBody)
        snake.score += 10 
        text.clear()
        text.write (snake.score, align = "center", font = ("roboto", 24,"normal"))     
        
    total= len(body)
    
    for i in range (total-1, 0, -1): #-1 count backward
        x = body[i - 1].xcor()
        y = body [i - 1].ycor()
        body[i].setpos(x , y)
    
    if (total > 0):
        x = snake.xcor()
        y = snake.ycor()
        body[0].setpos(x , y)

    move()    
    time.sleep(delay)

turtle.done()
