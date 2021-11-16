"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 11/08/2021

Description:
    Program that takes a string as input and converts
    it into pig latin.

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

def pig(str):
    l = []
    # Iterate over each word
    for w in str.split(" "):
        # Rearrange the word to match pig latin
        l.append(w[1 : len(w)] + w[0] + "ay")
    # Join the array with a whitespace separator
    return " ".join(l).capitalize()

def main():
    str = input("Enter a string: ")
    convert = pig(str)
    print(f"Pig latin: {convert}")


if __name__ == '__main__':
    main()
