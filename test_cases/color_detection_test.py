#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S3)
color_sensor.detectable_colors([Color.RED, Color.YELLOW])

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

while True:
    detected_color = color_sensor.color()

    if detected_color == Color.RED:
        robot.straight(10)
        robot.stop()
    elif detected_color == Color.YELLOW:
        robot.straight(10)
        robot.stop()
    else:
        robot.straight(500)
        robot.stop()

