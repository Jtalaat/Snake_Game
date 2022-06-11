from turtle import Turtle,Screen
import time
#To_do__1
#Create Snke and screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("John Snake Game")

screen.tracer(0)
F_position = [(0,0),(-20,0),(-40,0)]
segments = []
for p in F_position:
    segment = Turtle("square")
    segment.color('white')
    segment.penup()
    segment.goto(p)
    segments.append(segment)


game_is_on = True
while game_is_on:
    screen.update()
    for seg in segments:
        seg.forward(20)
        
        time.sleep(1)










#To_do__2
#Move the snake
#To_do__3
#control the snake
#To_do__4
#crete food model
#To_do__5
#score and speed
#To_do__6
#crete wall
#To_do__7
#die when eat your body

screen.exitonclick()