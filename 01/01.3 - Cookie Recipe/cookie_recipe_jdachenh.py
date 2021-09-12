"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 09/12/2021

Description:
    Program to calculate ingredient amounts for a cookie recipe.
    Takes the following inputs:
    -   How many cookies you want to make

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
    # Input
    # Take each input and cast to appropriate type
    numCookies = int(input("How many cookies do you want to make? "))

    # Algorithm
    # Calculate the values
    ratio = numCookies / 48
    sugarAmt = ratio * 1.75
    butterAmt = ratio * 1
    flourAmt = ratio * 2.5

    # Output
    # Format data to match the sample
    print(f"To make {numCookies} cookies, you will need:")
    print(f"  {sugarAmt:5.2f} cups of sugar")
    print(f"  {butterAmt:5.2f} cups of butter")
    print(f"  {flourAmt:5.2f} cups of flour")

if __name__ == '__main__':
    main()
