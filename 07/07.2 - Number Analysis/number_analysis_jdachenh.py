"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/25/2021

Description:
    Program that takes 10 numbers as inputs and determines the
    lowest, highest, sum, and average values.

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


def get_number_list():
    numbers = []
    # Take 10 inputs and append them to the list
    for i in range(1, 11):
        n = float(input(f"  number {i:2} of 10: "))
        numbers.append(n)
    return numbers


def main():
    print("Enter 10 numbers:")
    numbers = get_number_list()
    numbers.sort()
    # Get highest and lowest numbers
    low = numbers[0]
    high = numbers[9]
    # Calculate sum
    sum = 0
    for x in numbers:
        sum += x
    # Calculate average
    avg = sum / 10
    # Format and output
    print(f"Highest number: {high:.2f}")
    print(f"Lowest number: {low:.2f}")
    print(f"Total: {sum:.2f}")
    print(f"Average: {avg:.2f}")


if __name__ == '__main__':
    main()
