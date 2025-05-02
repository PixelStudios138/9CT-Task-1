#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
color_sensor1 = ColorSensor(Port.S4)
color_sensor2 = ColorSensor(Port.S3)
=======
color_sensor = ColorSensor(Port.S3)
gyro = GyroSensor(Port.S2)
>>>>>>> Stashed changes
=======
color_sensor = ColorSensor(Port.S3)
gyro = GyroSensor(Port.S2)
>>>>>>> Stashed changes

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

turn_angles = []

def get_color1():
    detected_color = color_sensor1.color()
    if detected_color is None:
        return None  
    return detected_color

<<<<<<< Updated upstream
<<<<<<< Updated upstream
def get_color2():
    detected_color = color_sensor2.color()
    if detected_color is None:
        return None
    return detected_color
=======
=======
>>>>>>> Stashed changes
<<<<<<< HEAD
=======
def turn_by_angle(angle): 
    robot.turn(angle)
    robot.straight(500)
    robot.stop()
    turn_angles.append(angle)
    navigate_course()
>>>>>>> Stashed changes

>>>>>>> 046b91db33ede9df79d2a21b51a860e8deda8bd3
def navigate_course():
    detected_color1 = get_color1()
    detected_color2 = get_color2()

<<<<<<< Updated upstream
<<<<<<< Updated upstream
    if detected_color1 in [Color.RED, Color.YELLOW]:
        while detected_color2 not in [Color.BLACK]:
            robot.straight()
        robot.straight(500)
    else:
        robot.turn(90)
        robot.straight(500)
=======
=======
>>>>>>> Stashed changes
    if detected_color in [Color.RED, Color.YELLOW]:
        # while black line has not been crossed, go forward.
        # when it's crossed, move forward 10cm
    else:
<<<<<<< HEAD
=======
        turn_by_angle(90)
>>>>>>> Stashed changes

>>>>>>> 046b91db33ede9df79d2a21b51a860e8deda8bd3

while True:
    navigate_course()
