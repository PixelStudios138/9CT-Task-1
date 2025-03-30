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

def turn_by_angle(angle): # function for allowing robot to turn around
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
    if Color.RED: # if block is red, it will return to start of course position
      return_to_start()
    elif Color.YELLOW: # if block is yellow, it will return to start of course position
      return_to_start()
    else: # if there is no red or yellow block, it will go straight, turn, and then go through navigation again until blocks are found
      robot.straight(500)        
      turn_by_angle(90)
      navigate_course()

def return_to_start(): # when block is found, it will be taken back to the position where the robot begun.
    for angle in reversed(turn_angles):  # Undo turns in reverse order
        turn_by_angle(-angle)  
    robot.straight(-1200)  

navigate_course()
