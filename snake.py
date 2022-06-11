from turtle import Turtle
start_Possition = [(0,0),(-20,0),(-40,0)]

class Snake :

    def __init__(self):
        self.segments = []
        self.createSnake()
    
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            newX = self.segments[seg-1].xcor()
            newY = self.segments[seg-1].ycor()
            self.segments[seg].goto(newX,newY)
        self.segments[0].forward(20)


    def createSnake(self):
        for p in start_Possition:
            segment = Turtle("square")
            segment.color('white')
            segment.penup()
            segment.goto(p)
            self.segments.append(segment)
