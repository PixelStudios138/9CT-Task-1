#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

turn_angles = []

def get_color():
    detected_color = color_sensor.color()
    if detected_color is None:
        return None  
    return detected_color

def turn_by_angle(angle): 
    robot.turn(angle)
    robot.stop()
    turn_angles.append(angle)
    navigate_course()

def navigate_course():
    detected_color = get_color()

    if detected_color in [Color.RED, Color.YELLOW]:
        robot.stop() # use gyro sensor to retrace steps, i.e moving block to starting position
    else:
        robot.straight(500)
        turn_by_angle(90)


while True:
    navigate_course()