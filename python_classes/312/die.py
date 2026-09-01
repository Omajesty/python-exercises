from random import randint


class Die:
    """Represent a die."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Roll the die and print the result."""
        result = randint(1, self.sides)
        print(result)


# 6-sided die
six_sided_die = Die()

print("6-sided die:")
for _ in range(10):
    six_sided_die.roll_die()


# 10-sided die
ten_sided_die = Die(10)

print("\n10-sided die:")
for _ in range(10):
    ten_sided_die.roll_die()


# 20-sided die
twenty_sided_die = Die(20)

print("\n20-sided die:")
for _ in range(10):
    twenty_sided_die.roll_die()