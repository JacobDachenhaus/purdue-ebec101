"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/18/2021

Description:
    Ouputs two random integers and prompts the user to enter
    the sum. If incorrect, it tells them the correct sum.

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


def random_number(numDigits):
    # Returns a random number [n|10^(n-1), 10^n - 1]
    # Examples:
    # n=1, [1, 9]
    # n=2, [10, 99]
    # n=3, [100, 999]
    return random.randint(10 ** (numDigits - 1), 10 ** (numDigits) - 1)


def main():
    # Get random numbers
    a = random_number(2)
    b = random_number(3)

    # Get the sum for later
    c = a + b

    # Prompt the user for input
    print(f"  {a:3}\n+ {b}\n-----\n= ", end='')
    answer = int(input())

    # Print outputs
    # Depending if the answer is correct or not
    print("Correct -- Good Work!") if answer == c else print(
        f"Incorrect. The correct answer is {c}.")


if __name__ == '__main__':
    main()
