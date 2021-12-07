"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 12/06/2021

Description:
    Takes inputs of sales data for every month and displays
    a pie chart visualizing that data.

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

COLORS = [
    '#4D4038', # CoalGray
    '#BAA892', # MoonDustGray
    '#5B6870', # EverTrueBlue
    '#6E99B4', # SlayterSkyBlue
    '#A3D6D7', # AmeliaSkyBlue
    '#085C11', # LandGrantGreen
    '#849E2A', # RossAdeGreen
    '#C3BE0B', # CeleryBogGreen
    '#E9E45B', # SpringFestGreen
    '#6B4536', # OakenBucketBrown
    '#B46012', # BellTowerBrick
    '#FF9B1A'  # MackeyOrange
]

MONTHS = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

def get_sales_data():
    sales_data = []
    for m in MONTHS:
        d = int(input(f'Enter the sales for {m}: '))
        sales_data.append(d)
    return sales_data

def main():
    sales_data = get_sales_data()
    fig, ax = plt.subplots()
    ax.set_title('Monthly Sales Values')
    ax.pie(sales_data, labels=MONTHS, colors=COLORS)
    plt.show()

if __name__ == '__main__':
    main()
