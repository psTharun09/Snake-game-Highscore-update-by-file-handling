from food import Food
from turtle import Turtle
ALIGN="center"
FONT=("Courier",15,"normal")

class scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt",mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"score:{self.score}",align=ALIGN,font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",align=ALIGN,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



