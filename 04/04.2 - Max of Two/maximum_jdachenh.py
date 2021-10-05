"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 04.2 - Maximum
Date: 10/04/2021

Description:
    Takes two integers and outputs the greater of the two.
    Takes the following inputs:
    - First integer
    - Second integer

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


def max_of_two(a, b):
    # Return the greater of a and b
    return a if (a > b) else b


def main():
    # Take two integers as inputs
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))

    # Figure out which one's greater
    max = max_of_two(a, b)

    # Format and output
    print(f"The number {max} is greater.")


if __name__ == '__main__':
    main()
