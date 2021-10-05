"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 04.5 - Prime List
Date: 10/04/2021

Description:
    Outputs a list of prime numbers up to the limit.
    Takes the following inputs:
    - Limit

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


def is_prime(num):
    prime = False
    # Determine if the number is prime
    if num > 1:
        # Loop through all previous numbers
        # If its evenly divisible, the number is not prime
        for i in range(2, num):
            if num % i == 0:
                # Number is not prime
                break
        else:
            # Number is prime
            prime = True
    return prime


def main():
    limit = int(input("Enter a positive integer: "))

    # Get a list of all the prime numbers up to the limit
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)

    # Loop through the list of primes
    # Format and output
    print(f"The primes up to {limit} are: {primes[0]}", end="")
    for i in range(1, len(primes)):
        print(f", {primes[i]}", end="")
    print()


if __name__ == '__main__':
    main()
