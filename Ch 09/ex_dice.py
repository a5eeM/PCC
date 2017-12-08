# Importing funtion randint() form module random

from random import randint

class Die():
    """
    A class representing a roll of a die.
    """

    def __init__(self, sides):
        """
        Initialize attributes.
        """
        self.sides = sides
    
    def roll_dice(self):
        """
        Prints a random number from a die of side 'sides'.
        """
        random_number = randint(1, self.sides)
        print("You rolled " + str(random_number) + " from your "  +
              str(self.sides) + "-sided die.")


six_sided_die = Die(6)
ten_sided_die = Die(10)
six_sided_die.roll_dice()
ten_sided_die.roll_dice()
