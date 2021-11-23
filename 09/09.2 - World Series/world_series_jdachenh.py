"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 09.2 - World Series
Date: 11/15/2021

Description:
    Program that takes a year and returns the team that won the
    World Series that year, along with that team's total number
    of wins.

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

def load_winners_data():
    d1 = {} # [name of the team] = number of times that team has won
    d2 = {} # [year] = name of the team that won that year

    with open('WorldSeriesWinners.txt') as f:
        lines = f.read().splitlines()

        for i, team in enumerate(lines):
            if team not in d1: d1[team] = 0
            year = i + 1903

            # No entries for 1904 or 1994
            if year >= 1904: year += 1
            if year >= 1994: year += 1

            d1[team] += 1
            d2[year] = team

    return (d1, d2)
    #END load_winners_data def

def main():
    (d1, d2) = load_winners_data()
    year = int(input('Enter a year in the range 1903 -- 2020: '))

    if year in d2:
        team = d2[year]
        print(f'  The {team} won the World Series in {year}.')
        print(f'  They have won the World Series {d1[team]} times.')
    elif year == 1904 or year == 1994:
        print(f'  The World Series wasn\'t played in the year {year}.')
    else:
        print(f'  Data for the year {year} is not included in this system.')
    #END main def


if __name__ == '__main__':
    main()
