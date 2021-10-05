"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 10/04/2021

Description:
    Takes five scores and outputs the letter grade for each of them.
    Then, average the scores and output the letter grade for the average.
    Takes the following inputs:
    - Five scores

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


def get_valid_score():
    score = float(input("Enter a score: "))
    # Validate the input
    if score < 0 or score > 100:
        print("  Invalid Input. Please try again.")
        score = get_valid_score()
    return score


def calc_average(scores):
    # Calculate the average for all scores in the list
    sum = 0
    for num in scores:
        sum += num
    return sum / len(scores)


def determine_grade(score):
    if score >= 91:
        return "A"
    if score >= 82:
        return "B"
    if score >= 73:
        return "C"
    if score >= 64:
        return "D"
    return "F"


def main():
    scores = []
    # Prompt the user for input, then output and append to list
    # Repeat 5 times
    for _ in range(5):
        score = get_valid_score()
        print(
            f"  The letter grade for {score:.1f} is {determine_grade(score)}.")
        scores.append(score)
    # Ouput the average of all the scores
    avg = calc_average(scores)
    print("\nResults:")
    print(f"  The average score is {avg:.2f}.")
    print(f"  The letter grade for {avg:.2f} is {determine_grade(avg)}.")


if __name__ == '__main__':
    main()
