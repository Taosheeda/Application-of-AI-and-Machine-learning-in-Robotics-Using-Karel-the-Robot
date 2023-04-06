from karel.stanfordkarel import *

"""
File: Mountain.py
----------------------------
Karel climbs a mountain of any size
and plants a beeper at the top
"""

def main():
    ascend_mountain()
    put_beeper()
    descend_mountain()

# defining ascend mountain
def descend_mountain():
    while front_is_clear():
        step_down()

#Teaching karel how to step down
def step_down():
    move()
    turn_right()
    move()
    turn_left()

# defining ascend mountain
def ascend_mountain():
    while front_is_blocked():
        step_up()

# defining step up
def step_up():    
    turn_left()
    move()
    turn_right()
    move()

# defining turn right
def turn_right():
    for i in range (3):
        turn_left()
        
        


# This is "boilerplate" code which launches your code
if __name__ == "__main__":
    run_karel_program()
