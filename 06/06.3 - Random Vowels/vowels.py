"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/18/2021

Description:
    Program that stores helper functions to draw vowels
    using turtle graphics.

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

STROKE_WIDTH = 9
X_HEIGHT = 60
ASC_HEIGHT = 30
KERNING = int(X_HEIGHT * 0.333)


def draw_a():
    # Width fix
    width(STROKE_WIDTH)
    # Draw
    [x, y] = pos()
    penup()
    goto(x, y + X_HEIGHT / 2)
    pendown()
    setheading(-90)
    circle(X_HEIGHT / 2)
    penup()
    goto(x + X_HEIGHT, y + X_HEIGHT)
    pendown()
    goto(x + X_HEIGHT, y)
    # Reposition
    penup()
    goto(x + X_HEIGHT + KERNING, y)


def draw_e():
    # Width fix
    width(STROKE_WIDTH)
    # Draw
    [x, y] = pos()
    penup()
    goto(x, y + X_HEIGHT / 2)
    pendown()
    goto(x + X_HEIGHT, y + X_HEIGHT / 2)
    setheading(90)
    circle(X_HEIGHT / 2, 315)
    # Reposition
    penup()
    goto(x + X_HEIGHT + KERNING, y)


def draw_i():
    # Width fix
    width(STROKE_WIDTH)
    # Draw
    [x, y] = pos()
    penup()
    goto(x, y + X_HEIGHT)
    pendown()
    goto(x, y)
    penup()
    goto(x, y + X_HEIGHT + ASC_HEIGHT)
    width(STROKE_WIDTH / 2)
    dot()
    # Reposition
    penup()
    goto(x + KERNING, y)


def draw_o():
    # Width fix
    width(STROKE_WIDTH)
    # Draw
    [x, y] = pos()
    penup()
    goto(x, y + X_HEIGHT / 2)
    pendown()
    setheading(-90)
    circle(X_HEIGHT / 2)
    # Reposition
    penup()
    goto(x + X_HEIGHT + KERNING, y)


def draw_u():
    # Width fix
    width(STROKE_WIDTH)
    # Draw
    [x, y] = pos()
    penup()
    goto(x, y + X_HEIGHT)
    pendown()
    goto(x, y + X_HEIGHT / 2)
    setheading(-90)
    circle(X_HEIGHT / 2, 180)
    penup()
    goto(x + X_HEIGHT, y + X_HEIGHT)
    pendown()
    goto(x + X_HEIGHT, y)
    # Reposition
    penup()
    goto(x + X_HEIGHT + KERNING, y)


def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """You can use this for your own testing."""
    pass


if __name__ == '__main__':
    # Do not change this part
    start()
    main()
    done()
