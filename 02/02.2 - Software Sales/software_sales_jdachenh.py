"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/20/2021

Description:
    Program to determine sale price after discounts.
    Takes the following inputs:
    - The number of packages being purchased

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


def main():
    # Input
    # Take each input and cast to appropriate type
    quantity = int(input("How many packages will be purchased: "))

    # Validate the inputs
    if quantity < 0:
        print("  Invalid Input!")
        return

    # Algorithm
    # Calculate the values
    discount = 0
    if quantity >= 100:
        discount = 0.45
    elif quantity >= 50:
        discount = 0.3
    elif quantity >= 25:
        discount = 0.2
    elif quantity >= 5:
        discount = 0.1

    price = quantity * 79 * (1 - discount)

    # Output
    # Format data to match the sample
    if discount > 0:
        print(f"  {discount * 100:.0f}% discount applied.")
    else:
        print("  No discount applied.")

    print(
        f"  The total price for purchasing {quantity} packages is ${price:,.2f}.")


if __name__ == '__main__':
    main()
