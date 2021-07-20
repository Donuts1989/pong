import turtle


class Paddle():
    speed = 20

    def __init__(self, wn, pos, player, ymax, ymin) -> None:
        self.wn = wn
        self.pos = pos
        self.player = player
        self.y = 0
        self.dy = 0
        self.ymax = ymax
        self.ymin = ymin

    def setup(self):
        # Paddle
        trace = turtle.Turtle()
        trace.speed(0)
        trace.shape("square")
        trace.color("white")
        trace.shapesize(stretch_wid=5, stretch_len=0.5)
        trace.penup()
        trace.goto(self.pos,0)

        self.trace = trace

        # Keyboard Binding
        self.wn.listen()

        if self.player == 1:
            self.wn.onkeypress(self.start_up, "w")
            self.wn.onkeypress(self.start_down, "s")
            self.wn.onkeypress(self.start_up, "W")
            self.wn.onkeypress(self.start_down, "S")
            self.wn.onkeyrelease(self.stop, "w")
            self.wn.onkeyrelease(self.stop, "s")
            self.wn.onkeyrelease(self.stop, "W")
            self.wn.onkeyrelease(self.stop, "S")
            

        else:
            self.wn.onkeypress(self.start_up, "Up")
            self.wn.onkeypress(self.start_down, "Down")
            self.wn.onkeyrelease(self.stop, "Up")
            self.wn.onkeyrelease(self.stop, "Down")

    def start_up(self):
        self.dy = Paddle.speed

    def start_down(self):
        self.dy = -Paddle.speed

    def stop(self):
        self.dy = 0

    def update(self):
        y = self.trace.ycor()
        if y + self.dy < self.ymax and y + self.dy > self.ymin:
            self.y = y + self.dy
            self.trace.sety(self.y)

    def reset(self):
        self.trace.sety(0)
        self.y = 0
        self.dy = 0