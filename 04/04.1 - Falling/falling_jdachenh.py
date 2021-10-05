"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 04.1 - Falling
Date: 10/04/2021

Description:
    Calculates the falling distance for an object from
    the 5 to 50 interval, incrementing by 5 each time.
    Uses a constant gravity value of the planet Venus.

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

# Set global value for gravity
g = 8.87


def falling_dist(time):
    # Define a helper function
    # Calculates the falling distance based on a given time
    return 0.5 * g * (time ** 2)


def main():
    print("Time (s)  Distance (m)")
    print("----------------------")
    # Loop from 5 to 50, incrementing by 5 each time
    for time in range(5, 51, 5):
        # Calculate the falling distance
        dist = falling_dist(time)
        # Format and output
        print(f"{time:8} {dist:13.1f}")


if __name__ == '__main__':
    main()
