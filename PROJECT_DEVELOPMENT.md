# 9CT1A_Assessment_Task1

## PROJECT_DEVELOPMENT.md

This markdown file will explain every file in this repository for the assessment task.

## Requirements

For this assessment task, we will need to write a program for the Lego EV3 robot to get it to sort lego bricks using the colour and gyroscopic sensor. It will need to use a colour sensor to stay within the playing field and detect a red block and a yellow block, then use the gyroscopic sensor to move the red and yellow blocks to their designated areas and to navigate around other blocks. The robot should:

- Move forward until an object is detected, or it falls outside the line
- If it's outside the playing area (shown by a black line), it should turn around and head back in
- When an object is detected, it should check the colour of it
- If the colour is red or yellow, it should:
    - Pick the block up
    - Put it down in the correct place
    - Continue navigating
- If the colour isn't red or yellow, it should ignore that block and navigate around it

### Functional Requirements

**Staying in the playing area:** When the robot detects the black line surrounding the playing field, the robot should stop, turn around 180 degrees, and drive straight, which should send it back in  
  
**Object Detection:** The robot should use the colour sensor to determine what type of block it sees. If it's red or yellow, it should use its arms to lift up the block and take it to the right spot. Otherwise, it should turn 90 degrees to the left or right, and travel around it.

**Moving:** When none of the above is in use, the robot should travel in a staight line until it detects an obstacle or the black line

### Use Cases

**Scenario 1:** The robot is driving around and goes over the black line  
**Inputs:** The colour sensor detects the black line  
**Action:** The robot stops, turns 180 degrees and keeps going  
**Expected Outcome** The robot re-enters the playing field and keeps going  
  
**Scenario 2:** The robot detects a block   
**Inputs:** The colour sensor detects a coloured object in front of it  
**Action:** If the colour is detected as red or yellow, it moves robot to designated position (200mm out of black line). If detected as a different colour, it continues moving onwards indifferently.  
**Expected Outcome** The robot sorts the block if it's red or yellow, and ingnores it if it's not  

**Scenario 3:** The robot has moved red or yellow block to designated position  
**Inputs:** The robot recognises it has moved 200mm beyond the black line  
**Action:** The object will be left at designated position, and the robot will turn around by rougly 180 degrees and then reenter the playing field.  
**Expected Outcome:** The robot, having left the red or yellow block in its deisgnated position, reenters the playing field and continues onward.  

**Test Cases:**

| Test Case              | Input                                | Expected Output                               |
|------------------------|--------------------------------------|-----------------------------------------------|
|Avoids Leaving          |Colour sensor detects black line      |Robot stops, turns 180 degrees, and keeps going|
|Detects red/yellow block|Colour sensor detects red/yellow block|Robot picks it up and puts it in the right spot|
|Has moved block         |Code has been fulfilled               |Robot turns 180 degrees and reenters field     |

### Non Functional Requirements

For each functional requirement, the robot should aim for these 3 requirements:  

- **Efficiency:** The robot should perform each task with maximum efficiency, such as turning the correct amount and properly picking up blocks on the first try  
- **Response Time:** The robot should respond to an input within 1 second. The quicker it does that, the better
- **Accuracy:** The robot should succeed in all of it's tasks on the first attempt. It shouldn't need to constantly make tiny rotations to get back in, or pick up the red and yellow block multiple times

## Pseudocode And Flowcharts

In order to get a proper look at how we're going to handle our code, there is nothing better than pseudocode and flowcharts. Here is a flowchart of how the code should work, and underneath will be the respective pseudocode: 

![Flowchart describing the process of the code used in the assessment task](/assessmenttaskpseudocode.png "Flowchart of Assessment Task")

Below is the pseudocode for scenario 1:
```
BEGIN Scenario 1
DECLARE coloursensorcolour: STRING

IF coloursensorcolour == "black"
    turnAround()
    moveForward()
ENDIF
OUTPUT "Inside black line!"
END Scenario 1
```

Below is the pseudocode for scenario 2:
```
BEGIN Scenario 2
DECLARE blockcoloursensorcolour: STRING
DECLARE linecoloursensorcolour: STRING

IF blockcoloursensorcolour == "red" OR blockcoloursensorcolour == "yelllow" 
    WHILE linecoloursensorcolour != "black"
        moveForward()
        IF linecoloursensorcolour == "black" 
            moveForward(200)
            stopMovement()
            ENDIF
        ENDWHILE

OUTPUT "Block is sorted!"
END Scenario 2
```

Below is the pseudocode for scenario 3:
```
BEGIN Scenario 3
DECLARE blockDelivered: BOOLEAN

WHILE blockDelivered
    turnAround()
    moveForward()
    blockDelivered = FALSE
ENDWHILE
OUTPUT "Back in playing field!"
END Scenario 3
```

## Code Tests

The test_cases folder has all the test cases created between the 28th of March and the 19th of May (due date).

### Driving Test

The first test we have is one for driving. This is practice created on the 28th of March to make sure that it works properly. This script gets the EV3 to move forward 1 metre, then back 1 metre, then turn 90 degrees to the left and then right. For this we hade to use the `robot.drive()` and `robot.turn()` feature. As an added bonus, we used the `ev3.speaker.beep()` function to get it to beep after every movement. Here is part of the script that gets the robot to move (ignoring the setup parts)

```
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
```

### Colour Detection Test

This second test is for the two colour sensors. Both functions will detect the colour in front of it. If there is, it will return that colour, and, if not, it will return nothing. The first colour sensor detects any coloured object, specifically a block, and, if it is yellow or red, will do turn in a complete revolution (if not, it will keep moving). The second colour sensor detects the black line and, if detected, will turn around to reenter the playing field.

```
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
```

### Gyro Test

This was the early code for using a gyro sensor to manage movements. It would use the gyro sensor to control the turns (as inputed in the navigate_course function), and store them in an array. Upon detecting a red or yellow block, it would retrace all the turns made, by doing the opposite of the stored turns. This code is incomplete, and has been left as such since we decided to change how we would move the blocks. 

```
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
```

### Random Turning Test

This block of code would make the turns random, with each turn anywhere from 1 to 120 degrees either clockwise or anticlockwise. This would allow the robot a wider coverage, yet we also found it to be too slow, and so we made the final code control the robot's movements through predetermined angles.

```
rand_num = random.uniform(0, 120) # turns anywhere within 120 degree scope
rand_num1 = random.choice(plus_or_minus)
if rand_num1 == 1: # clockwise turn
  robot.straight(120)
  robot.turn(rand_num)
elif rand_num1 == -1: # anticlockwise turn
  robot.straight(120)
  robot.turn(-rand_num)
else:
  print("error") # if failed to run
```

## Final Code

This is the end code that we have decided on. It will detect the colours in the same manner as was shown in the colour detection test. It will move around in something like a circle until it either goes over the black line (or into the black area), in which case it will turn around and reenter the field, or until it detects a red or yellow block (it will ignore other blocks), in which case it will move the block 200mm outside of the black line. 

```
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

def navigate_course():
    '''
    robot moves around the field until block is detected, then takes out of field, leaves in black area, and enters back into field
    '''
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
            robot.straight(30) 
            robot.turn(20)
            
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
```
 
## Conclusion

This markdown file has described everything required in this task, from functional and non functional requirements to pseudocode to the actual code and everything inbetween. We have poured our hearts and souls into this, and we hope it pays off. Thank you for your time.
