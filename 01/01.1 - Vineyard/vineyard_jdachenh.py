"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 01.1 - Vineyard
Date: 09/05/2021

Description:
    Program to calculate the number of grapevines to plant in each row.
    Takes the following inputs:
    -   The amount of space between the vines, in meters
    -   The amount of space used by an end-post assembly, in meters
    -   The length of the row, in meters

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


def main():
    print("Enter each of the following quantities in meters.")

    # Input
    # Take each input and cast to appropriate type
    s = int(input("  How much space should be between the vines? "))
    e = float(input("  How wide is the end-post assembly? "))
    r = int(input("  How long is this row? "))

    # Algorithm
    # Calculate the value
    v = (r - 2 * e) / s

    # Output
    # Format data to match the sample
    print(f"\nThis row has enough space for {int(v)} vine(s).")

if __name__ == '__main__':
    main()
