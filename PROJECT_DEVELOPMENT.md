# 9CT1A_Assessment_Task1

## PROJECT_DEVELOPMENT.md

This markdown file will explain every file in this repository for the assessment task.

## Tests

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
