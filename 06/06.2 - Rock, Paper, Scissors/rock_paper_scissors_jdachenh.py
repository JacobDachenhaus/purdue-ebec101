"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/18/2021

Description:
    Program that takes a user input of rock, paper, or scissors.
    Then it plays the classic game with you. If its a tie, the
    program will start again.

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


def get_computer_choice():
    # 1 = rock
    # 2 = paper
    # 3 = scissors
    c = random.randint(1, 3)
    if c == 1:
        return "rock"
    elif c == 2:
        return "paper"
    elif c == 3:
        return "scissors"


def get_player_choice():
    # Get user choice
    choice = input("Choose rock, paper, or scissors: ")

    # Validate the input
    if choice != "rock" and choice != "paper" and choice != "scissors":
        print("You made an invalid choice. Please try again.")
        return get_player_choice()

    return choice


def get_winner(pcChoice, usrChoice):
    # rock beats scissors
    # scissors beat paper
    # paper beats rock
    if pcChoice == usrChoice:
        return "tie"
    elif pcChoice == "rock" and usrChoice == "scissors":
        return "computer"
    elif pcChoice == "scissors" and usrChoice == "paper":
        return "computer"
    elif pcChoice == "paper" and usrChoice == "rock":
        return "computer"
    else:
        return "player"


def main():

    # Get computer choice
    pcChoice = get_computer_choice()

    # Get the user choice
    usrChoice = get_player_choice()

    # Get the winner
    winner = get_winner(pcChoice, usrChoice)

    # Display the choices
    print(f"  The computer chose {pcChoice}, and you chose {usrChoice}.")

    # Restart main if its a tie
    if winner == "tie":
        print("  Its a tie. Starting over.\n")
        return main()

    # Display the results
    if winner == "computer":
        print(
            f"  {pcChoice} beats {usrChoice}\n  You lost.  Better luck next time.")
    else:
        print(f"  {usrChoice} beats {pcChoice}\n  You won the game!")

    print("Thanks for playing.")


if __name__ == '__main__':
    main()
