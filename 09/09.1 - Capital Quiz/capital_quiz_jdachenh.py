"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 11/15/2021

Description:
    Program that quizzes the user on state captials.

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

import random

def get_state_data():
    d = {}

    # Load data from the provided file into a dictionary
    with open('state_capitals.txt') as f:
        data = f.read()
        lines = data.split('\n')

        for l in lines:
            if l == '': continue
            [capital, state] = l.split(', ')
            d[state] = capital # Use states as keys and capitals as values

    return d
    #END get_state_data def

def main():
    d = get_state_data()
    states = list(d.keys())

    random.shuffle(states) # Randomize the order

    numCorrect = 0
    numAsked = 0

    while len(states) > 0:
        state = states.pop(0)
        answer = input(f'What is the capital of {state} (enter 0 to quit)? ')
        
        if answer == '0': break
        numAsked += 1
        
        if answer.title() == d[state]: # Answers should not be case sensitive
            print('  That is correct!')
            numCorrect += 1
        else:
            print('  That is incorrect.')
            print(f'  The capital of {state} is {d[state]}.')
            states.append(state) # Append to ask again

    print(f'You answered {numCorrect} out of {numAsked} questions correctly.')
    #END main def

if __name__ == '__main__':
    main()
