"""
[2018-06-18] Challenge #364 [Easy] Create a Dice Roller

Input description

Your input will contain one or more lines, where each line will be in the form of "NdM"; for example:

3d6
4d12
1d10
5d4

If you've ever played D&D you probably recognize those, but for the rest of you, this is what those mean:

The first number is the number of dice to roll, the d just means "dice", it's just used to split up the two numbers, and the second number is how many sides the dice have. So the above example of "3d6" means "roll 3 6-sided dice". Also, just in case you didn't know, in D&D, not all the dice we roll are the normal cubes. A d6 is a cube, because it's a 6-sided die, but a d20 has twenty sides, so it looks a lot closer to a ball than a cube.

The first number, the number of dice to roll, can be any integer between 1 and 100, inclusive.

The second number, the number of sides of the dice, can be any integer between 2 and 100, inclusive.
Output description

You should output the sum of all the rolls of that specified die, each on their own line. so if your input is "3d6", the output should look something like

14

Just a single number, you rolled 3 6-sided dice, and they added up to 14.

"""

import random

random.seed()

diceRolls = []

# Pythonic Do While loop for inputting each number from a line.
while True:
    line = input()
    nums = line.split('d') # Split the numbers between the letter 'd'

    nums[0] = int(nums[0]) # Convert the strings to integers
    nums[1] = int(nums[1])
    
    if nums[0] < 1 or nums[0] > 100: # If first number does not meet requirement, move onto next input
        continue
    elif nums[1] < 2 or nums[1] > 100: # If second number does not meet requirement, move onto next input
        continue

    result = [] # Pick a number between the lowest possible value and the max.
    for i in range(nums[0]):
        result.append(random.randint(1, nums[1]))

    print(str(sum(result)) + ': ' +  str(result))
    
    if not line: # While condition of do while loop
        break
    else:
        diceRolls.append(line)

