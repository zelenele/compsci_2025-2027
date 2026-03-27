# IB DP CompSci - Imports Exercise

# ---------------------------------------------------------------------------
# PART 1 – STANDARD LIBRARY IMPORTS
# ---------------------------------------------------------------------------

# TODO:

# - Import the math module
# - Print:
#   1) sqrt(81)
#   2) pi rounded to 3 decimal places

# TODO: write your imports here
import math
# TODO: write your prints here
print(math.sqrt(81))
number_of_places = 6
formated_pi = format(math.pi, f".{number_of_places}")
print(formated_pi)

# ---------------------------------------------------------------------------
# PART 2 – FROM ... IMPORT ...
# ---------------------------------------------------------------------------

# TODO:
# - Import sqrt and floor from math using: from math import ...
# - Use them to:
#   1) compute sqrt(50)
#   2) floor the result

# TODO: write your imports here

value = 50
# TODO: compute root
root = math.sqrt(50)
# TODO: compute floored
floored = math.floor(50)

print("sqrt(50) =", root)
print("floor(sqrt(50)) =", floored)


# ---------------------------------------------------------------------------
# PART 3 – ALIASES
# ---------------------------------------------------------------------------

# TODO:
# - Import random as rnd
# - Simulate rolling a 6-sided die 10 times
# - Store the results in a list and print it

# TODO: write your imports here
import random as rand
rolls = []
# TODO: add 10 random ints from 1 to 6
for i in range (10):
    rolls.append(rand.randint(1,6))
print("Rolls:", rolls)


# ---------------------------------------------------------------------------
# PART 4 – IMPORTING YOUR OWN MODULE
# ---------------------------------------------------------------------------

# There is a file in this folder called my_utils.py
# TODO:
# - Import my_utils
# - Use:
#   1) my_utils.shout("hello")
#   2) my_utils.is_even(123)
#   3) my_utils.clamp(200, 0, 100)

# TODO: write your import here

print("Shout:", None)   # TODO
print("Is even:", None) # TODO
print("Clamp:", None)   # TODO


# ---------------------------------------------------------------------------
# PART 5 – DEBUGGING IMPORTS (CHALLENGE)
# ---------------------------------------------------------------------------

# TODO:
# - What happens if you create a file named random.py in this folder?
# - Why does that break `import random`?
# - Write your answer as a multi-line string below:
# - Below is an example of a multi-line string:
answer = """
TODO: write your explanation here.
"""

print(answer)