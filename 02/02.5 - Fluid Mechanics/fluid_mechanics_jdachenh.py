"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/20/2021

Description:
    Program to calculate Reynolds number for fluid flow
    through a pipe.
    Takes the following inputs:
    - The temperature in celcius
    - The velocity of water in m/s or ft/s
    - The pipe's diameter

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
    # Take each input and cast to appropriate type
    temp = int(input("Enter the temperature in \u00B0C as 5, 10, or 15: "))
    vel = float(input("Enter the velocity of water in the pipe: "))
    d = float(input("Enter the pipe's diameter: "))

    # Determine the kv
    if temp == 5:
        kv = 1.49e-6
    elif temp == 10:
        kv = 1.31e-6
    elif temp == 15:
        kv = 1.15e-6

    # Calculate the values
    re = (vel * d) / kv

    # Format data to match the sample
    print(f"At {temp:.1f}\u00B0C, the Reynolds number for flow at {vel} m/s in a {d} m diameter pipe is {re:.2e}.")


if __name__ == '__main__':
    main()
