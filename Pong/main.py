from turtle import Screen
from paddle import Paddle
from screensetup import ScreenSetup
from ball import Ball
from scoreboard import Scoreboard
import time

WALL_TOP = 200
WALL_BOTTOM = -200
WALL_RIGHT = 350
WALL_LEFT = -350
STARTING_POSITION_Player_1 = [(WALL_LEFT + 20, -40), (WALL_LEFT + 20, -20), (WALL_LEFT + 20, 0), (WALL_LEFT + 20, 20), (WALL_LEFT + 20, 40)]
STARTING_POSITION_Player_2 = [(WALL_RIGHT - 20, -40), (WALL_RIGHT - 20, -20), (WALL_RIGHT - 20, 0), (WALL_RIGHT - 20, 20), (WALL_RIGHT - 20, 40)]



def reset_game():
    paddle_1.reset()
    paddle_2.reset()
    ball.reset()
    ball.random_direction()
    ball.pu()
    time.sleep(2)


screen = Screen()
screen.register_shape("ManuBall.gif")
screen.setup(width=WALL_RIGHT * 2, height=WALL_TOP * 2)
screen.bgcolor("black")
screen.title("ManuPong")

screen.tracer(0)
t = ScreenSetup()
scoreboard = Scoreboard()
paddle_1 = Paddle(STARTING_POSITION_Player_1)
paddle_2 = Paddle(STARTING_POSITION_Player_2)
ball = Ball()


screen.listen()
screen.onkeypress(paddle_2.up, "Up")
screen.onkeypress(paddle_2.down, "Down")
screen.onkeypress(paddle_1.up, "w")
screen.onkeypress(paddle_1.down, "s")

game_is_on = True
continue_game = True

while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # detect collision with wall
    if ball.ycor() > WALL_TOP - 20 or ball.ycor() < WALL_BOTTOM + 20:
        ball.reflexion_wall()

    # detect collision with paddle
    for segments in paddle_1.segments:
        if ball.distance(segments) < 20:
            ball.reflexion_paddle()

    for segments in paddle_2.segments:
        if ball.distance(segments) < 20:
            ball.reflexion_paddle()

    # detect missing paddle
    if ball.xcor() < WALL_LEFT:
        scoreboard.score_up_2()
        reset_game()

    if ball.xcor() > WALL_RIGHT:
        scoreboard.score_up_1()
        reset_game()

    #check if game has ended
    if scoreboard.score_1 == 10 or scoreboard.score_2 == 10:
        t.clear()
        if scoreboard.score_1 > scoreboard.score_2:
            scoreboard.game_over("Player 1")
        elif scoreboard.score_1 < scoreboard.score_2:
            scoreboard.game_over("Player 2")
        game_is_on = False


screen.mainloop()
