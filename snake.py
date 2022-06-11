from turtle import Turtle
start_Possition = [(0,0),(-20,0),(-40,0)]
step = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake :

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
    
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            newX = self.segments[seg-1].xcor()
            newY = self.segments[seg-1].ycor()
            self.segments[seg].goto(newX,newY)
        self.segments[0].forward(step)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def createSnake(self):
        for p in start_Possition:
            segment = Turtle("square")
            segment.color('white')
            segment.penup()
            segment.goto(p)
            self.segments.append(segment)
