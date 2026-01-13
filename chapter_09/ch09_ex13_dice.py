# Exercise 9-13 From 'Python Crash Course'
# 13-01-2026 G. Melief

# Exercise with importing classes from the standard library

from random import randint

class Die:
    """A class emulating a dice"""


    def __init__(self, sides=6):
        """Initialize dice attributes"""
        self.sides = sides

    def roll_dice(self):
        """Print a random number between 1 and the number of sides the dice has"""
        roll = randint(1, self.sides)
        print(f"\tYou rolled {roll}!")

# Make a 6-sided dice and roll it 10 times
dice_6 = Die()
print(f"\nThe dice you're playing with has {dice_6.sides} sides.")
for rolls in range(10):
    dice_6.roll_dice()

# Make a 10-sided dice and roll it 10 times
dice_10 = Die(10)
print(f"\nThe dice you're playing with has {dice_10.sides} sides.")
for rolls in range(10):
    dice_10.roll_dice()

# Make a 20-sided dice and roll it 10 times
dice_20 = Die(20)
print(f"\nThe dice you're playing with has {dice_20.sides} sides.")
for rolls in range(10):
    dice_20.roll_dice()