import turtle

s = turtle.Screen()
s.listen()
t = turtle.Turtle()
t.speed(0)
def goTur(x, y):
    t.goto(x,y)
s.onclick(goTur)

turtle.done()