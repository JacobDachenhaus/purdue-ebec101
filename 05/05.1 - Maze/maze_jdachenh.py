"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 05.1 - Maze
Date: 10/11/2021

Description:
    Program that takes a turtle and navigates it
    out of a maze. Draws a green line that shows the
    path it took.

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
    bgpic('maze.png')
    shape('turtle')
    color('green')
    width(5)


SQUARE_SIZE = 12


def turnLeft():
    lt(90)


def turnRight():
    rt(90)


def moveForward(squares=1):
    forward(squares * SQUARE_SIZE)


def main():
    """Write your code below this line."""
    moveForward()
    turnRight()
    moveForward()
    turnLeft()
    moveForward(2)
    turnLeft()
    moveForward(4)
    turnRight()
    moveForward(4)
    turnRight()
    moveForward(2)
    turnLeft()
    moveForward(4)
    turnRight()
    moveForward(2)
    turnLeft()
    moveForward(4)
    turnRight()
    moveForward(4)
    turnLeft()
    moveForward(4)
    turnLeft()
    moveForward(5)
    turnRight()
    moveForward(2)


# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
