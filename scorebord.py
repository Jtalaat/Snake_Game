from re import L
from turtle import Turtle

class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_score

    def update_score(self):
        self.write(f"score :{self.score}",align="center",font=("Arial",24,"normal"))

    def gameOver(self):
        self.write(f"Game Over score is {self.score}",align="center",font=("Arial",24,"normal"))


    def increasescore(self):
        self.score +=1
        self.clear()
        self.update_score()