import turtle


class Scoreboard():
    win_condition = 1000
    player_1 = "Player A"
    player_2 = "Player B"

    def __init__(self, on_finish) -> None:
        self.on_finish = on_finish
    
        self.score_a = 0
        self.score_b = 0

    def setup(self):
    
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0,260)
        pen.write(f'{self.player_1}: 0               {self.player_2}: 0', align="center", font=("Courier", 24, "normal"))

        self.pen = pen

    def update(self):
        self.pen.clear()
        self.pen.write(f'{self.player_1} {self.score_a}               {self.player_2} {self.score_b}', align="center", font=("Courier", 24, "normal"))

        if self.score_a == Scoreboard.win_condition or self.score_b == Scoreboard.win_condition:
            self.on_finish()

    def announce_winner(self):
        self.pen.clear()
        self.pen.goto(0,0)
        self.pen.write("WINNER".format(), align="center", font=("Courier", 100, "normal"))
        self.pen.goto(0,-50)
        winner = 1 if self.score_a > self.score_b else 2
        self.pen.write("Player {}".format(winner), align="center", font=("Courier", 40, "normal"))