"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 08.6 - Step Counter
Date: 11/08/2021

Description:
    Program that calculates the average number of steps taken
    in each month given a file named steps.txt that tracks
    the steps taken each day for 365 days, with each number
    on a separate line.

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
    # 2d array with month name and number of days
    months = [
        ["January", 31],
        ["February", 28],
        ["March", 31],
        ["April", 30],
        ["May", 31],
        ["June", 30],
        ["July", 31],
        ["August", 31],
        ["September", 30],
        ["October", 31],
        ["November", 30],
        ["December", 31]
    ]

    counter = 0

    # Read the file
    with open("steps.txt") as fo:
        lines = fo.readlines()

    print("The average steps taken each month were:")

    for [month, numDays] in months:
        # Sum the lines that correspond to that month
        sum = 0
        for i in range(numDays):
            sum += int(lines[i + counter].strip("\n"))

        # Format and output
        avg = sum / numDays
        print(f"{month.rjust(10)} : {avg:.2f}")

        # Increment the counter
        counter += numDays

if __name__ == '__main__':
    main()
