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

def get_color1():
    ''' 
    gets colour value from color_sensor1 (block detector)
    '''
    detected_color = color_sensor1.color()
    if detected_color is None: # returns nothing if no colour is detected
        return None  
    return detected_color # returns detected colour value

def get_color2():
    '''
    gets colour from colour_sensor2 (black line detector)
    '''
    detected_color = color_sensor2.color() 
    if detected_color is None: # returns nothing if no colour is detected
        return None
    return detected_color # returns detected colour value

def colour1_test():
    '''
    tests colour_sensor1 (block detector) to see if blocks can be properly identified
    '''

    detected_color1 = get_color1()
    
    if detected_color1 in [Color.RED, Color.YELLOW]:  # turns around if red or yellow block is detected
        robot.turn(360)
    else:
        robot.straight(50) # keeps moving if block is undetected

def colour2_test():
    '''
    tests colour_sensor2 (line detector) to see if it knows when breaching black line
    '''
    
    detected_color2 = get_color2()

    if detected_color2 == Color.BLACK: # if breaching black line, robot turns and reenters playing field
        robot.turn(180)
        robot.straight(200)
    else: # keeps slowly moving (to take account of delay factor) until black line is reached
        robot.straight(20)
    
while True:
    colour1_test()
