"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 08.3 - File Stats
Date: 11/08/2021

Description:
    Program that takes a hardcoded text file and counts the number
    of words and lines, and then calculates the average number of
    words per line.

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
    wordcount = 0
    linecount = 0

    # Open the file for reading
    with open("frontiero_v_richardson.txt") as fo:
        lines = fo.readlines()

        # Store the linecount
        linecount = len(lines)

        # Iterate over each line to determine the word count
        for line in lines:
            line = line.replace("\n", "")

            # If the line is empty, skip this iteration
            if len(line) == 0: continue

            words = line.split(" ")

            for word in words:
                if len(word) > 0: wordcount += 1

    # Calculate the average words per line
    avgwords = wordcount / linecount

    # Format output
    print(f"Total number of words: {wordcount}")
    print(f"Total number of lines: {linecount}")
    print(f"Average number of words per line: {avgwords:.1f}")


if __name__ == '__main__':
    main()
