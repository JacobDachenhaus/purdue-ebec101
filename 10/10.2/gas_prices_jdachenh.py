"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 12/06/2021

Description:
    Program that takes data from a provided text file
    and plots its values.

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

import matplotlib.pyplot as plt

def get_contents():
    with open('2008_Weekly_Gas_Averages.txt', 'r') as f:
        # Get the file contents as a string
        # Split string into a list using \n as the delimiter
        # Iterate over each value and type cast them into floats
        # Return the new list
        return [float(l) for l in f.read().splitlines()]

def main():
    contents = get_contents()
    fig, ax = plt.subplots()

    # Use [1, 53)
    ax.plot(range(1, 53), contents)

    # Customize the plot display
    ax.set_title('2008 Weekly Gas Prices')

    ax.set_xlabel('Weeks (by number)')
    ax.set_xlim(1, 52)
    ax.set_xticks([10, 20, 30, 40, 50])

    ax.set_ylabel('Average Price (dollars/gallon)')
    ax.set_ylim(1.5, 4.25)
    ax.set_yticks([1.5, 2, 2.5, 3, 3.5, 4])

    ax.grid()

    # Show the plot
    plt.show()

if __name__ == '__main__':
    main()
