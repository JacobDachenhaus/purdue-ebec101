"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/21/2021

Description:
    Program that returns a filtered list with multiples of N. 
    Does not take any inputs.

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


def multiples_of(n, list):
    # Store empty list for later
    multi = []
    # Filter multiples of N
    for x in list:
        if x % n == 0:
            multi.append(x)
    return multi


def main():
    # This is all hard coded
    # Not good practice at all
    n = 13
    list = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]
    multi = multiples_of(n, list)

    # Output the data
    print("Original list of numbers:")
    print(f"  {list}")
    print(f"Numbers in the list that are multiples of {n}:")
    print(f"  {multi}")


if __name__ == '__main__':
    main()
