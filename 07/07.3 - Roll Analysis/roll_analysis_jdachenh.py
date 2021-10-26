"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/25/2021

Description:
    Program that counts the frequency of values from 1_000_000
    rolls of 2d6 dice.

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


def roll_d6():
    return randint(1, 6)


def get_2d6_rolls(numRolls):
    rolls = []
    for _ in range(numRolls):
        # Roll 2d6 and add them together
        rolls.append(roll_d6() + roll_d6())
    return rolls


def main():
    # Hard code the number of rolls
    numRolls = 1_000_000

    rolls = get_2d6_rolls(numRolls)

    print("Roll  Frequency")
    for n in range(2, 13):
      # Count the number of occurences of n in rolls
      count = rolls.count(n)
      # Calculate the frequency
      freq = count / numRolls
      # Format and output
      print(f" {n:2}    {freq * 100:5.2f}%")


if __name__ == '__main__':
    main()
