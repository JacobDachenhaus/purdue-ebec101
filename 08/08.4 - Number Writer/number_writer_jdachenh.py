"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 08.4 - Number Writer
Date: 11/08/2021

Description:
    Program that takes a number of random integers to generate,
    and writes that many random integers (each on a seperate line)
    to a file called random_numbers.txt.

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

from random import randint

def main():
    n = int(input("How many numbers would you like? "))

    # Open file for writing
    with open("random_numbers.txt", "w") as fo:
        for _ in range(n):
            # Get a random int [1019, 1215] and write it, with a trailing newline
            r = randint(1019, 1215)
            fo.write(f"{r}\n")

if __name__ == '__main__':
    main()
