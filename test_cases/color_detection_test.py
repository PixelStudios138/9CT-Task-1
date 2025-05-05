#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
color_sensor1 = ColorSensor(Port.S1)
color_sensor2 = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

def get_color1():
    detected_color = color_sensor1.color()
    if detected_color is None:
        return None  
    return detected_color

def get_color2():
    detected_color = color_sensor2.color()
    if detected_color is None:
        return None
    return detected_color

def navigate_course():
    detected_color1 = get_color1()
    detected_color2 = get_color2()

    if detected_color1 in [Color.RED, Color.YELLOW]:
        while detected_color2 not in [Color.BLACK]:
            detected_color2 = get_color2()
            robot.straight(30)
            if detected_color2 == Color.BLACK:
                print("over the line")
                robot.stop()
                robot.turn(200)
                robot.straight(100)

    else:
        detected_color1 = get_color1()
        detected_color2 = get_color2()

        if detected_color2 == Color.BLACK:
            robot.stop()
            robot.turn(200)
            robot.straight(70)
        else:
            if detected_color1 in [Color.RED, Color.YELLOW]:
                while detected_color2 not in [Color.BLACK]:
                    detected_color2 = get_color2()
                    robot.straight(30)
                    if detected_color2 == Color.BLACK:
                        print("over the line")
                        robot.stop()
                        robot.turn(200)
                        robot.straight(100)
            else:
                robot.straight(70)
                robot.turn(15)
while True:
    navigate_course()
