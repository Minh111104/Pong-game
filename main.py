from turtle import Screen
from paddle import Paddle
from ball import Ball
# slow the ball down
import time
from scoreboard import Scoreboard

screen = Screen()

# create the screen
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
# turn off tracer
screen.tracer(0)

# create two paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# create the ball object
ball = Ball()

# move the paddle
screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# create the scoreboard object
scoreboard = Scoreboard()

# update and refresh the screen after turn tracer off
game_is_on = True

while game_is_on:
    # time.sleep(0.1)
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball needs to bounce
        ball.bounce_y()

    # detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        # track the score
        scoreboard.l_point()

    # detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        # track the score
        scoreboard.r_point()

screen.exitonclick()
