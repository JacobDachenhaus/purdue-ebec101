"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 10/11/2021

Description:
    Program that takes user input for the number of points
    on a star, then draws that star.

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

# Also the radius of a circle enclosed by the star.
SIDE_LENGTH = 60


def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    width(7)
    penup()
    goto(0, -SIDE_LENGTH)  # Start at the bottom of the star.
    pendown()


def main():
    """Write your code below this line."""
    # Take user input for num points
    num = int(input("How many points? "))
    # Calculate the inner and outer angles
    thetaA = 360.0 / num
    thetaB = 2 * thetaA
    # Rotate the pointer to level
    rt(90 - thetaA)
    # Set pen and fill colors
    color("black")
    fillcolor("pink")
    # Begin fill
    begin_fill()
    # Draw each segment of the star
    for _ in range(0, num):
        forward(SIDE_LENGTH)
        lt(180 - thetaA)
        forward(SIDE_LENGTH)
        rt(180 - thetaB)
    # Fill object
    end_fill()


# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
