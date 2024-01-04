import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10) 
s.bgcolor("red")#Background color
s.title("Project 1")
t.shapesize(5,1,5) #large, weight, border

t.pensize(2)
t.backward(100)

t.circle(80)
t.shapesize(3,3,3)
t.fillcolor("orange")
t.pencolor("white")
t.goto(-30,-30)
t.color("white", "orange")
t.goto(80,-50)
turtle.done()