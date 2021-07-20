from ball import Ball
from timer import Timer
import turtle
import winsound
from paddle import Paddle
from scoreboard import Scoreboard


class Game():
    height = 600
    width = 800

    def setup(self):

        wn = turtle.Screen()
        wn.title("Pong by @Donuts23")
        wn.bgcolor("black")
        wn.setup(width=Game.width, height=Game.height)
        wn.tracer(0)

        self.wn = wn

        self.timer = Timer(self.delete_timer)
        self.timer.setup()

        # Paddles
        self.paddle_a = Paddle(wn, -350, 1, Game.height/2 - 39, -Game.height/2 + 50)
        self.paddle_b = Paddle(wn, 350, 2, Game.height/2 - 39, -Game.height/2 + 50)
        self.paddle_a.setup()
        self.paddle_b.setup()

        # Ball
        self.ball = Ball(Game.height/2, -Game.height/2)
        self.ball.setup()

        # Scoreboard
        self.scoreboard = Scoreboard(self.end_game)
        self.scoreboard.setup()

    def update(self):
        wn = self.wn
        paddle_a = self.paddle_a
        paddle_b = self.paddle_b
        ball = self.ball

        wn.update()
        paddle_a.update()
        paddle_b.update()

        if self.timer:
            self.timer.update()
            
            return

        ball.update()
               
        # Border checking
        # TODO: Calculate edges and positions by code - Dynamically.

        if ball.y > 290:
            ball.y = 290
            self.collide_wall()

        if ball.y < -290:
            ball.y = -290
            self.collide_wall()

        if ball.x > 390:
            self.scoreboard.score_a += 1
            self.score()

        if ball.x < -390:
            self.scoreboard.score_b += 1
            self.score()

        # Ball Collides with Paddle
        if (ball.x > 330) and (ball.y < paddle_b.y + 50 and ball.y > paddle_b.y - 50):
            ball.x = 330
            self.collide_paddle()
            
        if (ball.x < -330) and (ball.y < paddle_a.y + 50 and ball.y > paddle_a.y - 50):
            ball.x = -330
            self.collide_paddle()

    def score(self):
        self.ball.reset()
        self.paddle_a.reset()
        self.paddle_b.reset()
        winsound.PlaySound("Sound/bounce_border.wav", winsound.SND_ASYNC)
        self.scoreboard.update()
        self.timer = Timer(self.delete_timer)
        self.timer.setup()

    def collide_paddle(self):
        self.ball.dx *= -1
        self.ball.set_speed(1.05*abs(self.ball.dx))
        winsound.PlaySound("Sound/bounce_paddle.wav", winsound.SND_ASYNC)

    def collide_wall(self):
        self.ball.dy *= -1
        winsound.PlaySound("Sound/bounce_paddle.wav", winsound.SND_ASYNC)

    def delete_timer(self):
        self.timer = None

    def end_game(self):

        #TODO: Clear Screen for Winner Announcement
        self.scoreboard.announce_winner()

    # def button(x,y):
    #     if x < 50 and x > -50 and y < 50 and y > -50:
    #         print(f"Your coordinates are: ({x}, {y}).")
    # turtle.onscreenclick(button, 1, add=False)
    # turtle.done()
        

