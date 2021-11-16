"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 08.5 - Number Reader
Date: 11/08/2021

Description:
    Program that reads the file generated from the previous
    exercise, and calculates certain statistics regarding the
    file contents.

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
    min = 0
    max = 0
    sum = 0

    # Open the file for reading
    with open("random_numbers.txt") as fo:
        lines = fo.readlines()
        count = len(lines)

        # Store the first integer as the min & max
        n1 = int(lines[0].strip("\n"))
        min = n1
        max = n1
        sum += n1

        # Iterate over each integer
        # Check if its less than the current min or greater than the current max
        for i in range(1, count):
            n = int(lines[i].strip("\n"))
            if n < min: min = n
            if n > max: max = n
            sum += n

    # Calculate the average
    avg = sum / count

    # Format and output
    print(f"{count:,} numbers were read from the file.")
    print(f"Min: {min:,}")
    print(f"Max: {max:,}")
    print(f"Sum: {sum:,}")
    print(f"Avg: {avg:,.1f}")

if __name__ == '__main__':
    main()
