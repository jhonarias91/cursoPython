import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10)
t.begin_fill()
t.circle(10)
t.end_fill()
t.begin_fill()
t.color("white","red")
t.circle(5)
t.end_fill()

#t.shape("square")
#t.shape("arrow")
#t.shape("circle")
#t.shape("triangle")
t.shape("turtle")

t.pencolor("orange")
t.penup()
t.pendown()
t.forward(10)
t.penup()
t.forward(10)
t.pendown()
t.forward(10)

t.undo() #Ctrl Z
t.clear() #Clean background keeping turtle pos
t.reset() #rebot to begining

t.forward(20)
t.color("red")
t.stamp()
t.color("green")
t.forward(40)
turtle.done()