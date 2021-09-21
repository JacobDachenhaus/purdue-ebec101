"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/20/2021

Description:
    Program to display the time in days, hours, minutes, and seconds.
    Takes the following inputs:
    -   The time in seconds

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
    time = int(input("Please enter a time in seconds: "))

    # Check if less than 60
    if (time < 60):
        print(f"  {time} seconds is less than one minute.")
        return

    # Calculate the values
    d = time // 86400
    h = (time % 86400) // 3600
    m = (time % 3600) // 60
    s = time % 60

    # Format data to match the sample
    print(f"  {time:,} seconds is: ", end="")

    if d:
        print(f"{d} day(s)", end="")

    if h:
        if d:
            if m or s:
                print(", ", end="")
            else:
                print(" and ", end="")
        print(f"{h} hour(s)", end="")

    if m:
        if d or h:
            if s:
                print(", ", end="")
            else:
                print(" and ", end="")
        print(f"{m} minute(s)", end="")

    if s:
        if d or h or m:
            print(" and ", end="")
        print(f"{s} second(s)", end="")

    print(".")


if __name__ == '__main__':
    main()
