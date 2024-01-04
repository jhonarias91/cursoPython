import turtle

#Call to print a window
s = turtle.Screen()
t = turtle.Turtle()
a = 0
while a < 5:
    t.forward(80)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(80)
    t.left(135)
    t.forward(520)
    t.reset()
    a+=1

turtle.done()