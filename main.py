#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

turn_angles = []

def turn_by_angle(angle): # function for allowing robot to turn around
    robot.turn(angle)
    robot.stop()
    turn_angles.append(angle)  # Record the turns

def navigate_course():
    if Color.RED: # if block is red, it will return to start of course position
        robot.stop
    # return_to_start()
    elif Color.YELLOW: # if block is yellow, it will return to start of course position
        robot.stop
    # return_to_start()
    else: # if there is no red or yellow block, it will go straight, turn, and then go through navigation again until blocks are found
      robot.straight(500)        
      turn_by_angle(90)
      navigate_course()

def return_to_start(): # when block is found, it will be taken back to the position where the robot begun.
    for angle in reversed(turn_angles):  # reverses its course to start position
        turn_by_angle(-angle)  
    navigate_course()

navigate_course()