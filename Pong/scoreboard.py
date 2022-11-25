from turtle import Turtle
WALL_TOP = 200
WALL_BOTTOM = -200
WALL_RIGHT = 350
WALL_LEFT = -350


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.ht()
        self.pu()
        self.color("white")
        self.goto(x=0, y=WALL_TOP - 40)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score_1}      {self.score_2}", move=False, align="center", font=('Courier', 25, 'bold'))

    def game_over(self, winner):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=('Courier', 25, 'bold'))
        self.goto(0, -30)
        self.write(f"{winner} wins!", move=False, align="center", font=('Courier', 20, 'normal'))

    def score_up_1(self):
        self.score_1 += 1
        self.clear()
        self.update_scoreboard()

    def score_up_2(self):
        self.score_2 += 1
        self.clear()
        self.update_scoreboard()