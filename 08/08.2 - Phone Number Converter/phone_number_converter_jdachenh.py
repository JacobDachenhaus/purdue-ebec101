"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 11/08/2021

Description:
    Program that takes an alphanumeric phone number and
    converts its alphabetic characters to digits.

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

def convert_number(phoneNum):
    # Make the string lowercase to ignore capitalization
    phoneNum = phoneNum.lower()
    newPhoneNum = ""

    # Replace each alphabetic character with its corresponding digit
    for char in phoneNum:
        if char == "a" or char == "b" or char == "c":
            newPhoneNum += "2"
        elif char == "d" or char == "e" or char == "f":
            newPhoneNum += "3"
        elif char == "g" or char == "h" or char == "i":
            newPhoneNum += "4"
        elif char == "j" or char == "k" or char == "l":
            newPhoneNum += "5"
        elif char == "m" or char == "n" or char == "o":
            newPhoneNum += "6"
        elif char == "p" or char == "q" or char == "r" or char == "s":
            newPhoneNum += "7"
        elif char == "t" or char == "u" or char == "v":
            newPhoneNum += "8"
        elif char == "w" or char == "x" or char == "y" or char == "z":
            newPhoneNum += "9"
        else:
            newPhoneNum += char

    return newPhoneNum

def main():
    phoneNum = input("Enter a telephone number: ")
    newPhoneNum = convert_number(phoneNum)
    print(f"The phone number is {newPhoneNum}")


if __name__ == '__main__':
    main()
