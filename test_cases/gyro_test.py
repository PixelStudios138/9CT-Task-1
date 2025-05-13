'''
This is the code for turning using the gyro sensor, which was decided against.
'''

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, Colorsensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
gyro = GyroSensor(Port.S2)

turn_angles = []

def turn_by_angle(angle): 
'''
gyro controls turning based on inputed angle, and turns are recorded in turn_angles array. This allows all turns to be retraced later.
'''

    gyro.reset_angle(0)
    if angle > 0:  # clockwise 
        while gyro.angle() < angle:
            robot.drive(0, 50)
    else:  # counterclockwise
        while gyro.angle() > angle:
            robot.drive(0, -50)
    robot.stop()
    turn_angles.append(angle)  # Record the turn

def navigate_course():
'''
  Returns to starting position to drop red or yellow block (if identified), otherwise continues moving around playing field
'''

    if Color.RED: # if block is red, it will return to start of course position
      return_to_start()
    elif Color.YELLOW: # if block is yellow, it will return to start of course position
      return_to_start()
    else: # if there is no red or yellow block, it will go straight, turn, and then go through navigation again until blocks are found
      robot.straight(500)        
      turn_by_angle(90)
      navigate_course()

def return_to_start():
'''
Retraces all previous movements, back to starting position
'''

    for angle in reversed(turn_angles):  # reverses its course to start position
        turn_by_angle(-angle)  
    navigate_course()

navigate_course()
