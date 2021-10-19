"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 06.4 - Arch Spiral
Date: 10/18/2021

Description:
    Program that draws an archimedean spiral with 6 full revolutions.

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
from math import pi, cos, sin


def toRadians(theta):
    return theta * (pi / 180)


def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    width('5')


def main():
    theta = 0

    pendown()

    while theta <= 6 * 360:
        # Calculate values
        thetaRad = toRadians(theta)
        thetaPiSq = theta / (pi ** 2)
        x = int(thetaPiSq * cos(thetaRad))
        y = int(thetaPiSq * sin(thetaRad))

        # Move the pen
        goto(x, y)

        # Increment theta
        theta += 2


if __name__ == '__main__':
    # Do not change this part
    start()
    main()
    done()
