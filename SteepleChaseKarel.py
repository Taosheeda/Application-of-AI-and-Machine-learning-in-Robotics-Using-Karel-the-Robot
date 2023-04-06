from karel.stanfordkarel import *

"""
File: SteepleChaseKarel.py
--------------------------
Karel runs a steeple chase the is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""

"""
To run a race that is 9 avenues long, we need to move
forward or jump hurdles 8 times.
"""
def main():
  for i in range(8):
    ascend_hurdle()
    move()
    descend_hurdle()

#defining ascend_hurdle()
def ascend_hurdle():
    turn_left()
    while right_is_blocked():
        move()
    turn_right()

#defining turn_right()
def turn_right():
    for i in range(3):
        turn_left()

# defining descend_hurdle()
def descend_hurdle():
    turn_right()
    move_to_wall()
    turn_left()

# defining move_to_the_wall()
def move_to_wall():
    while front_is_clear():
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
