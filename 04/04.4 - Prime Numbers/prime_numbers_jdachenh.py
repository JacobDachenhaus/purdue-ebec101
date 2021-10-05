"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 10/04/2021

Description:
    Program that takes a positive integer as an input and determines if
    its prime. Continues asking for numbers until the user inputs -1 to
    quit the program.

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


def is_prime(num):
    prime = False
    # Determine if the number is prime
    if num > 1:
        # Loop through all previous numbers
        # If its evenly divisible, the number is not prime
        for i in range(2, num):
            if num % i == 0:
                # Number is not prime
                break
        else:
            # Number is prime
            prime = True
    return prime


def main():
    # Keep looping until the user inputs -1
    while True:
        # Prompt the user for input
        num = int(input("Enter a positive integer (-1 to quit): "))
        # Quit the program
        if num == -1:
            break
        # Format and output
        print(f"  {num} is prime!") if is_prime(
            num) else print(f"  {num} is not prime.")


if __name__ == '__main__':
    main()
