import turtle
from time import monotonic as time
import winsound

class Timer():
    def __init__(self, on_finish) -> None:
        self.last_time = time()
        self.counter = 3
        self.on_finish = on_finish

    def setup(self):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0,50)
        self.pen = pen
        self.draw()

    def update(self):
        current_time = time()

        if current_time - self.last_time >= 0.8:
            self.last_time = current_time
            self.counter -= 1
            
            if self.counter > 0:
                self.draw()

        if self.counter == 0:
            self.pen.clear()
            winsound.PlaySound("Sound/bounce_paddle.wav", winsound.SND_ASYNC)
            self.on_finish()

    def draw(self):
        self.pen.clear()
        self.pen.write(self.counter, align="center", font=("Courier", 150, "normal"))
        winsound.PlaySound("Sound/bounce_paddle.wav", winsound.SND_ASYNC)

