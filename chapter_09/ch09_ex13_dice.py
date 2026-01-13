# Exercise 9-13 From 'Python Crash Course'
# 13-01-2026 G. Melief

# Exercise with importing classes from the standard library

from random import randint

class Die:
    """A class emulating a dice"""


    def __init__(self, sides=6):
        """Initilize dice attributes"""
        self.sides = sides

    def roll_dice(self):
        """Print a random number between 1 and the number of sides the dice has"""
        print(randint(1, self.sides))

dice_6 = Die()
dice_6.roll_dice()