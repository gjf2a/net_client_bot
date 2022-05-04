#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import threading


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left = Motor(Port.A)
right = Motor(Port.D)
sonar = UltrasonicSensor(Port.S4)

import sys
print("Python version", sys.version)

# Server class
class MessageHandler(threading.Thread):
    def __init__(self):
        self.go = True
        self.server = socket.

    def run(self):
        print("Starting thread")
        x = 0
        while True:
            x += 1
            if x % 1000 == 0:
                self.go = not self.go
        print("looped ", x, "times")

mh = MessageHandler()
mh.start()

# Write your program here.
ev3.speaker.beep()

while True:
    if mh.go:
        if sonar.distance() < 150:
            left.run(-360)
            right.run(360)
        else:
            left.run(360)
            right.run(360)
    else:
        left.stop()
        right.stop()