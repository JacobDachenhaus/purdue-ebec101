"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 01.2 - Interest
Date: 09/12/2021

Description:
    Program to calculate compund interest over time.
    Takes the following inputs:
    -   The amount of principal originally deposited into the account
    -   The annual interest rate paid by the account, in percent
    -   The number of times per year that the interest is compound
    -   The number of years the account will be left to earn interest

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
    print("Please enter the following quantities.")
    
    # Input
    # Take each input and cast to appropriate type
    p = int(input("  How much is the initial deposit? "))
    r = float(input("  What is the annual interest rate in percent? ")) / 100
    n = int(input("  How many times per year is the interest compounded? "))
    t = float(input("  How many years will the account earn interest? "))

    # Algorithm
    # Calculate the value
    fv = p * (1 + r / n) ** (n * t)

    # Output
    # Format data to match the sample
    print(f"\nAt the end of {t:.1f} years, this account will be worth ${fv:,.2f}.")

if __name__ == '__main__':
    main()
