import turtle
import random
class TurtleRace():
   
    _XSTART = -300
    _XEND = 300
    _YT1=145
    _YT2=-10

    def start(self):
        s = turtle.Screen()
        t1 = turtle.Turtle()
        t2 = turtle.Turtle()
        s.title("Turtle Race")

        t1.shape("turtle")
        t2.shape("turtle")
        t1.penup()
        t2.penup()
        t1.setx(self._XEND)
        t1.sety(80)
        t2.setx(self._XEND)
        t2.sety(-80)

        t1.speed(0)
        t1.pendown()
        t1.color("green", "green")
        t1.circle(70)

        t2.speed(0)
        t2.pendown()
        t2.color("orange", "orange")
        t2.circle(70)

        t1.penup()
        t1.setx(self._XSTART)
        t1.sety(self._YT1)
        t2.penup()
        t2.setx(self._XSTART)
        t2.sety(self._YT2)
        t1.pendown()
        t2.pendown()

        self.play(t1, t2)

        turtle.done()

    def play(self, t1, t2):
        dice = [1 ,2, 3, 4, 5, 6]
        t1.speed(1)
        t2.speed(1)
        currX1 = self._XSTART       
        currX2 = self._XSTART
        while (currX1 < self._XEND and currX2 < self._XEND):
            pos1 = random.randint(0,5)    
            currX1 += dice[pos1]*10
            if (currX1 > self._XEND):
                t1.setx(self._XEND)
            else:    
                t1.forward(dice[pos1]*10)

            pos2 = random.randint(0,5)    
            currX2 += dice[pos2]*10
            if (currX2 > self._XEND):
                t2.setx(self._XEND)
            else:    
                t2.forward(dice[pos2]*10)  

        t1.speed(0)
        t2.speed(0)
        t1.setx(self._XSTART)
        t1.sety(self._YT1)
        t2.setx(self._XSTART)
        t2.sety(self._YT2)

        if ( currX1 > currX2):
            t1.write("Winner", align="center", font=("Arial", 16, "normal"))
        elif (currX1 < currX2):
            t2.write("Winner", align="center", font=("Arial", 16, "normal"))
        else:
            t1.write("Both win", align="center", font=("Arial", 16, "normal"))
            t2.write("Both win", align="center", font=("Arial", 16, "normal"))


race = TurtleRace()

race.start()
   