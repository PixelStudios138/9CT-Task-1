#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
import random

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
color_sensor1 = ColorSensor(Port.S1)
color_sensor2 = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

plus_or_minus = [1, -1]

def get_color1(): # gets colour value from color_sensor1 (block detector)
    detected_color = color_sensor1.color()
    if detected_color is None: # returns nothing if no colour is detected
        return None  
    return detected_color # returns detected colour value

def get_color2(): # gets colour from colour_sensor2 (black line detector)
    detected_color = color_sensor2.color() 
    if detected_color is None: # returns nothing if no colour is detected
        return None
    return detected_color # returns detected colour value

def navigate_course():
    detected_color1 = get_color1() # block detector variable
    detected_color2 = get_color2() # line detector variable

    if detected_color1 in [Color.RED, Color.YELLOW]:
        while detected_color2 not in [Color.BLACK]: # once block is detected, move forward until black line is reached
            detected_color2 = get_color2()
            robot.straight(30)
            if detected_color2 == Color.BLACK: # once black line is reached, move forward by 200, place down block, and then move back into the field
                print("over the line")
                robot.stop()
                robot.turn(200)
                robot.straight(100)

    else:
        detected_color1 = get_color1() # block detector variable
        detected_color2 = get_color2() # line detector variable

        if detected_color2 == Color.BLACK: # if it reaches the black area, it will turn back and enter back into the field
            robot.stop()
            robot.turn(200)
            robot.straight(70)
        else: # moves around until block is detected
            robot.straight(70) 
            robot.turn(35)
            
            if detected_color1 in [Color.RED, Color.YELLOW]: # same purpose as this code above
                while detected_color2 not in [Color.BLACK]:
                    detected_color2 = get_color2()
                    robot.straight(30)
                    if detected_color2 == Color.BLACK:
                        print("over the line")
                        robot.stop()
                        robot.turn(200)
                        robot.straight(100)
while True:
    navigate_course() # begins with navigate course function
