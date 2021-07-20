import turtle

def sign(x):
    return bool(x > 0) - bool(x < 0)

class Ball():
    speed = 10

    def __init__(self, ymax, ymin) -> None:
        self.y = 0
        self.x = 0
        self.dy = Ball.speed
        self.dx = Ball.speed
        self.ymax = ymax
        self.ymin = ymin

    def setup(self):
        trace = turtle.Turtle()
        trace.speed(0)
        trace.shape("square")
        trace.color("white")
        trace.shapesize(stretch_wid=0.8, stretch_len=0.8)
        trace.penup()
        trace.goto(0,0)

        self.trace = trace

    def update(self):
        self.trace.setx(self.x)
        self.trace.sety(self.y)

    def reset(self):
        self.x = 0
        self.y = 0
        self.trace.setx(0)
        self.trace.sety(0)
        self.dx *= -1
        self.set_speed(Ball.speed)

    def set_speed(self, speed):
        self.dy = sign(self.dy)*speed
        self.dx = sign(self.dx)*speed

    def physics_update(self, delta):
        if self.y >= self.ymax or self.y <= self.ymin:
            self.dy *= -1
        self.y += self.dy*delta
        self.x += self.dx*delta
