#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from server import MessageHandler


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left = Motor(Port.A)
right = Motor(Port.D)
sonar = UltrasonicSensor(Port.S4)

import sys
print("Python version", sys.version)

mh = MessageHandler()
mh.ev3 = ev3
mh.start()

ev3.speaker.beep()

while True:
    if mh.go:
        if sonar.distance() < 250:
            left.run(-360)
            right.run(360)
        else:
            left.run(360)
            right.run(360)
    else:
        left.stop()
        right.stop()