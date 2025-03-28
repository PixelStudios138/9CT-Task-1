#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

robot.straight(1000)
ev3.speaker.beep()

robot.straight(-1000)
ev3.speaker.beep()

robot.turn(90)
ev3.speaker.beep()

robot.turn(-90)
ev3.speaker.beep()