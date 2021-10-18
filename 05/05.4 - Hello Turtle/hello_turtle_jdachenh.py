"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 05.4 - Hello Turtle
Date: 10/11/2021

Description:
    Program that draws text with a limited selection of characters.
    Currently hard-coded to draw "hello turtle"

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
    setup(600, 400)
    width(9)


CAP_SIZE = 60
NUM_SEGMENTS = 16
THETA = 360.0 / NUM_SEGMENTS
SEGMENT_LENGTH = (3.14 * CAP_SIZE) / NUM_SEGMENTS


def drawCircle(numSegments, h=90, dir=1):
    seth(h)
    pd()
    for _ in range(numSegments):
        rt(dir * THETA)
        forward(SEGMENT_LENGTH)


def draw_e():
    [x, y] = pos()
    pu()
    setpos(x, y + (CAP_SIZE / 2) + (SEGMENT_LENGTH / 2))
    pd()
    seth(0)
    forward(CAP_SIZE)
    drawCircle(NUM_SEGMENTS - 2, dir=-1)
    # Reset pos
    pu()
    setpos(x + CAP_SIZE, y)


def draw_h():
    [x, y] = pos()
    pu()
    setpos(x, y + (CAP_SIZE * 2))
    pd()
    setpos(x, y)
    pu()
    setpos(x, y + (CAP_SIZE / 2) + (SEGMENT_LENGTH / 2))
    pd()
    drawCircle(int(NUM_SEGMENTS / 2))
    setpos(x + CAP_SIZE, y)


def draw_l():
    [x, y] = pos()
    pu()
    setpos(x, y + (CAP_SIZE * 2))
    pd()
    setpos(x, y)


def draw_o():
    [x, y] = pos()
    pu()
    setpos(x, y + (CAP_SIZE / 2) + (SEGMENT_LENGTH / 2))
    pd()
    drawCircle(NUM_SEGMENTS)
    pu()
    setpos(x + CAP_SIZE, y)


def draw_r():
    [x, y] = pos()
    pu()
    setpos(x, y + CAP_SIZE)
    pd()
    setpos(x, y)
    pu()
    setpos(x, y + (CAP_SIZE / 2) + (SEGMENT_LENGTH / 2))
    pd()
    drawCircle(int(NUM_SEGMENTS / 4))
    pu()
    setpos(x + (CAP_SIZE / 2), y)


def draw_t():
    [x, y] = pos()
    pu()
    setpos(x + (CAP_SIZE / 2), y + (CAP_SIZE * 2))
    pd()
    setpos(x + (CAP_SIZE / 2), y)
    pu()
    setpos(x, y + (CAP_SIZE * 1.5))
    pd()
    setpos(x + CAP_SIZE, y + (CAP_SIZE * 1.5))
    pu()
    setpos(x + CAP_SIZE, y)


def draw_u():
    [x, y] = pos()
    pu()
    setpos(x, y + CAP_SIZE)
    pd()
    setpos(x, y + (CAP_SIZE / 2) - (SEGMENT_LENGTH / 2))
    drawCircle(int(NUM_SEGMENTS / 2), h=270, dir=-1)
    pu()
    setpos(x + CAP_SIZE, y + CAP_SIZE)
    pd()
    setpos(x + CAP_SIZE, y)


def drawText(text, kern=(CAP_SIZE * 0.35), lh=(CAP_SIZE * 2.3)):
    # Keep track of y level
    [startX, startY] = pos()
    dy = 0
    for c in text:
        # Draw letters
        if c == "e":
            draw_e()
        elif c == "h":
            draw_h()
        elif c == "l":
            draw_l()
        elif c == "o":
            draw_o()
        elif c == "r":
            draw_r()
        elif c == "t":
            draw_t()
        elif c == "u":
            draw_u()
        # Draw newlines
        elif c == "\n":
            dy += lh
            pu()
            setpos(startX, startY - dy)
            continue
        # Draw spaces (or invalid characters)
        else:
            [lineX, lineY] = pos()
            pu()
            setpos(lineX + CAP_SIZE, lineY)
            continue
        # Add kerning after each letter
        [lineX, lineY] = pos()
        pu()
        setpos(lineX + kern, lineY)


def main():
    pu()
    setpos(-3.35 * CAP_SIZE, CAP_SIZE)
    drawText(" hello\nturtle")


# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
