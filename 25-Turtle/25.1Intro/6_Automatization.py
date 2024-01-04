import turtle

s = turtle.Screen()
t = turtle.Turtle()

distance = 10
t.speed(0)
for i in range (1,9):
    t.forward(distance)
    t.right(90)
    if ( i % 4 == 0):
        distance += 10

t.speed(10)
radio = 5
while radio <= 15:
    turtle.circle(radio)
    radio += 5

turtle.done()