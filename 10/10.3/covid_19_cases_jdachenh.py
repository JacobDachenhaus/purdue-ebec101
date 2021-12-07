"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 10.3 - Covid 19 Cases
Date: 12/06/2021

Description:
    Program that takes covid case data
    and sums positive cases into cumulative values by date,
    then displays a visualization of the data.

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

import datetime
import matplotlib.pyplot as plt

def get_covid_data():
    # Store future dictionary keys and values as lists
    dts = []
    cum_pos_thousands = []

    with open('indiana_covid_19_data_fall_2021.txt') as f:
        lines = f.read().splitlines()
        # Iterate over each line in the file
        for i in range(len(lines)):
            # Split lines at whitespace characters
            date, tests, pos, deaths = lines[i].split(' ')
            
            # Convert date to datetime
            dt = datetime.date(*[int(v) for v in date.split('-')])
            dts.append(dt)

            # Convert pos to thousands
            pos_thousands = round(int(pos) / 1000, 3)

            # Handle edge cases
            if i == 0:
                cum_pos_thousands.append(pos_thousands)
                continue

            # Get the previous value to calculate the cumulative
            prev = cum_pos_thousands[i - 1]
            cum_pos_thousands.append(prev + pos_thousands)

    # Construct two lists into dictionary
    covid_data = dict(zip(dts, cum_pos_thousands))
    return covid_data

def main():
    covid_data = get_covid_data()

    # Make the plot
    fig, ax = plt.subplots()
    ax.bar(covid_data.keys(), covid_data.values(), width=1)

    # Customize the plot
    ax.set_title('Positive COVID-19 Cases in Indiana')

    ax.set_xlabel('Date')
    fig.autofmt_xdate()

    ax.set_ylabel('Number of Cases (in thousands)')
    ax.set_ylim(0)
    ax.set_yticks([0, 200, 400, 600, 800, 1_000, 1_200])

    # Display the plot
    plt.show()

if __name__ == '__main__':
    main()
