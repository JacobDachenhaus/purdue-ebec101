"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 12/06/2021

Description:
    Program that calculates and plots the y=sin(x) and y=cos(x)
    functions from x=[0, pi/2].

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
import numpy as np

def main():
    # Calculate the x and y values at each step
    step = 0.001
    x = np.arange(0, 2 * np.pi + step, step) # [start, stop)
    y1 = np.sin(x)
    y2 = np.cos(x)

    ##
    #  Make the plot
    ##
    fig, ax = plt.subplots()

    ax.plot(x, y1, color='r')
    ax.plot(x, y2, color='b')

    ##
    #  Customize the plot
    ##

    # Format the axes
    for spine in ('top', 'right'):
        ax.spines[spine].set_visible(False)
    for spine in ('bottom', 'left'):
        ax.spines[spine].set_position('zero')

    # Set ticks and labels
    ax.set_xticks([np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
    ax.set_xticklabels(['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'])
    
    ax.set_yticks([-1, 1])

    ##
    #  Display the plot
    ##
    plt.show()

if __name__ == '__main__':
    main()
