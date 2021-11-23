"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 09.4 - File Analysis
Date: 11/22/2021

Description:
    Program that analyses the two provided files xian_1.txt and
    xian_2.txt, and creates new files representing their
    statistics. Includes the word frequency from both files, as
    well as the common words and uncommon words

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

from string import punctuation

def get_words(filename):
    words = []
    with open(filename) as file:
        for line in file.readlines():
            for word in line.split(' '):
                words.append(word.lower().strip(punctuation + '\n'))
    return filter(len, words) # Remove empty strings from list

def get_word_frequency(words):
    uniques = {}
    for word in words:
        uniques[word] = uniques[word] + 1 if word in uniques else 1
    return uniques

def main():
    # Use helper fn to parse file contents into a list of words
    xian_1_words = get_words('xian_1.txt')
    xian_2_words = get_words('xian_2.txt')

    # Use helper fn to count the frequency of each word
    xian_1_word_frequency = get_word_frequency(xian_1_words)
    xian_2_word_frequency = get_word_frequency(xian_2_words)

    # Use AND operator to get words that appear in both
    common_words = set(xian_1_word_frequency) & set(xian_2_word_frequency)

    # Use XOR operator to get words that appear in either but not both
    eitherbutnotboth = set(xian_1_word_frequency) ^ set(xian_2_word_frequency)

    # 1. xian_1_word_frequency.txt
    with open('xian_1_word_frequency.txt', 'w') as file:
        lines = []
        for key in sorted(xian_1_word_frequency):
            lines.append(f'{key}: {xian_1_word_frequency[key]}')
        file.write('\n'.join(lines))

    # 2. xian_2_word_frequency.txt  
    with open('xian_2_word_frequency.txt', 'w') as file:
        lines = []
        for key in sorted(xian_2_word_frequency):
            lines.append(f'{key}: {xian_2_word_frequency[key]}')
        file.write('\n'.join(lines))

    # 3. common_words.txt
    with open('common_words.txt', 'w') as file:
        file.write('\n'.join(sorted(common_words)))

    # 4. eitherbutnotboth.txt
    with open('eitherbutnotboth.txt', 'w') as file:
        file.write('\n'.join(sorted(eitherbutnotboth))) 
    #END main def

if __name__ == '__main__':
    main()
