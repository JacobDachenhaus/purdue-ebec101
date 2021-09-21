"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/20/2021

Description:
    Program that helps determine whether a specific year
    was a leap year.
    Takes the following inputs:
    -   The year to determine the number of days

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
    year = int(input("Please input a year: "))
    num_days = 28

    # Algorithm
    # Determine if its a leap year
    if year % 100 == 0:
        if year % 400 == 0:
            num_days = 29
    elif year % 4 == 0:
        num_days = 29

    # Output
    # Format data to match the sample
    print(f"In the year {year}, February has {num_days} days.")


if __name__ == '__main__':
    main()
