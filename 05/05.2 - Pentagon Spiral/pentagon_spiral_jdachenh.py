
"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 05.2 - Pentagon Spiral
Date: 10/11/2021

Description:
    Program that draws a pentagon spiral with 32 sides.

Contributors:
    None

My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [x] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

from turtle import *


def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    width(5)


def main():
    """Write your code below this line."""
    # Loops from 1 to 33 (32 iterations)
    for i in range(1, 34):
        # Draws the line forward 8 * i pixels
        forward(8 * i)
        # Turns 72 deg left
        lt(72)


# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
