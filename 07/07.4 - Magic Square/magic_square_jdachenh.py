"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 07.4 - Magic Square
Date: 10/25/2021

Description:
    Program that checks hardcoded 2d arrays to see if they 
    are magic squares.

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

def print_square(square):
  size = len(square)
  for i in range(size):
    str = f"  {square[i][0]}"
    for j in range(1, size):
      str += f" {square[i][j]}"
    print(str)

def is_magic(square):
  # Get the size of the square
  size = len(square)

  # Calculate the maximum value
  max = size ** 2

  # Calculate the magic number
  magicNum = 0
  for x in square[0]:
    magicNum += x

  # Check values for duplicates or out of range
  dict = []
  for i in range(size):
    for j in range(size):
      val = square[i][j]
      if 1 > val > max or dict.count(val) > 0:
        return False
      dict.append(val)

  # Check rows
  for i in range(size):
    sumRow = 0
    for j in range(size):
      sumRow += square[i][j]
    if sumRow != magicNum:
      return False

  # Check cols
  for i in range(size):
    sumCol = 0
    for j in range(size):
      sumCol += square[j][i]
    if sumCol != magicNum:
      return False
  
  # Check diag
  # Top left to bottom right
  sumDiag = 0
  for i in range(size):
    sumDiag += square[i][i]
  if sumDiag != magicNum:
    return False
  # Top right to bottom left
  sumDiag = 0
  for i in range(size):
    sumDiag += square[i][-(i + 1)]
  if sumDiag != magicNum:
    return False

  # Passed all tests!
  return True

      

def main():
  # Squares to check
    squares = [
      [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
      [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
      [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    ]

    for square in squares:
      print("Your square is:")
      print_square(square)

      if is_magic(square):
        print("It is a Lo Shu magic square!\n")
      else:
        print("It is not a Lo Shu magic square.\n")


if __name__ == '__main__':
    main()
