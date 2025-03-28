#Import the necessary files
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

#Store the EV3 Brick in a variable for easier usage
ev3 = EV3Brick()

#Initialise the left and rigt motor
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

#Set up the wheels and motors so that they'll drive
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

#Go forward by a metre and then beep
robot.straight(1000)
ev3.speaker.beep()

#Go backwards by a metre and then beep
robot.straight(-1000)
ev3.speaker.beep()

#Turn 90 degrees clockwise and then beep
robot.turn(90)
ev3.speaker.beep()

#Turn 90 degrees anticlockwise and then beep
robot.turn(-90)
ev3.speaker.beep()