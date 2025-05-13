'''
The following code is for random turning, which was decided against.
'''

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
