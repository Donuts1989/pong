from time import time_ns
from game import Game
import sys

FPS = 60
PHYS_FPS = 500
counter = 0

pong = Game()
pong.setup()

def log(msg):
    sys.stdout.write("\r%s" % msg)
    sys.stdout.flush()

# Main game loop
last_time = time_ns()*10**-9
phys_time_update = time_ns()*10**-9

while True:
    current_time = time_ns()*10**-9

    if current_time - phys_time_update > 1/PHYS_FPS:
        delta = current_time - phys_time_update
        phys_time_update = current_time
        counter += 1
        pong.physics_update(delta*FPS)

    if current_time - last_time > 1/FPS:
        delta = current_time - last_time

        #FIXME: Measure true FPS.
        last_time = current_time
        counter -= 1
        pong.update()
    
    log(counter)