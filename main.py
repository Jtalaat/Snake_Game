import imp
from operator import le
from turtle import Turtle,Screen
import time
from snake import Snake
#To_do__1
#Create Snke and screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("John Snake Game")

screen.tracer(0)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)











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