"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/18/2021

Description:
    Program that draws all 5 vowels in a random order each
    runtime using turtles.

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

import random
import vowels


def main():
    # Store all draw functions in an array
    # and randomize their order
    drawArr = random.sample([vowels.draw_a, vowels.draw_e,
               vowels.draw_i, vowels.draw_o, vowels.draw_u], 5)

    # Run each function
    for fn in drawArr:
      fn()


if __name__ == '__main__':
    main()
