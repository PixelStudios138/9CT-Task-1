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
  
**Scenario 2:** The robot is detects a block  
**Inputs:** The ultrasonic sensor detects the brick, the colour sensor detects the colour  
**Action:** The robot checks what colour it is, and if it's red or yellow, picks it up and moves it to the designated area, if not, it turns 90 degrees and keeps going  
**Expected Outcome** The robot sorts the block if it's red or yellow, and ingnores it if it's not  

**Test Cases:**

| Test Case              | Input                                | Expected Output                               |
|------------------------|--------------------------------------|-----------------------------------------------|
|Avoids Leaving          |Colour sensor detects black line      |Robot stops, turns 180 degrees, and keeps going|
|Detects red/yellow block|Colour sensor detects red/yellow block|Robot picks it up and puts it in the right spot|
|Detects other block     |Colour sensor detects other block     |Robot stops, turns 90 degrees, and keeps going |

### Non Functional Requirements

For each functional requirement, the robot should aim for these 3 requirements:  

- **Efficiency:** The robot should perform each task with maximum efficiency, such as turning the correct amount and properly picking up blocks on the first try  
- **Response Time:** The robot should respond to an input within 1 second. The quicker it does that, the better
- **Accuracy:** The robot should succeed in all of it's tasks on the first attempt. It shouldn't need to constantly make tiny rotations to get back in, or pick up the red and yellow block multiple times

## Pseudocode And Flowcharts

In order to get a proper look at how we're going to handle our code, there is nothing better than pseudocode and flowcharts. Here is a flowchart of how the code should work, and underneath will be the respective pseudocode: 

![Flowchart describing the process of the code used in the assessment task](/assessmenttaskpseudocode.png "Flowchart of Assessment Task")

```
BEGIN
DECLARE bricksfound: INTEGER
bricksfound = 0
DECLARE isOutside: BOOLEAN
DECLARE coloursensorcolour: STRING

WHILE bricksfound < 2:
    IF isInside = false:
        turnAround()
    ENDIF
    IF coloursensorcolour = "red" OR coloursensorcolour = "yellow:
        moveblock()
    ENDIF
ENDWHILE
OUTPUT "All blocks sorted!"
END
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

## Conclusion

This markdown file has described everything required in this task, from functional and non functional requirements to pseudocode to the actual code and everything inbetween. I have poured my heart and soul into this, and I hope it pays off. Thank you for your time.
