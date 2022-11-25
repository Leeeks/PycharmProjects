from turtle import Turtle

with open("data.txt") as data:
    contents = int(data.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.ht()
        self.pu()
        self.color("white")
        self.goto(x=0, y=280)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", move=False, align="center", font=('Courier', 14, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", move=False, align="center", font=('Courier', 25, 'bold'))

    def score_up(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()