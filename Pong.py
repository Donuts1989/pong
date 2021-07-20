from time import monotonic
from game import Game
import sys

FPS = 60

pong = Game()
pong.setup()

def log(msg):
    sys.stdout.write("\r%s" % msg)
    sys.stdout.flush()

# Main game loop
last_time = 0

while True:
    current_time = monotonic()

    if current_time - last_time > 1/FPS:
        delta = current_time - last_time

        #FIXME: Measure true FPS.
        log(1/delta)

        last_time = current_time
        pong.update()