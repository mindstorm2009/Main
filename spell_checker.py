"""
    File: spell_checker.py
    Author: Nicholas Curl
    Description: project
"""

import math
import punctuation_process as pu

# Global variable for the alphabet
ALPHABET = tuple(chr(code) for code in range(ord("a"), ord("z") + 1))


def fix_by_adjacent(dictionary, adj_letters, letters):
    """Spell checks to see if the adjacent letters form the correct word"""
    previous = ""
    fix_word = ""
    fixed = False
    for i in range(len(letters)):
        # Skips the characters ' and _ in a word, since it is not in the adjacent letters dictionary
        if letters[i] == "'" or letters[i].isdigit() or letters[i] == "_" or letters[i] == "’":
            previous += letters[i]
            continue
        adj = adj_letters[letters[i]]
        # Runs through each adjacent letter given the letter from the word and determines if it is in the dictionary
        for element in adj:
            new_word = previous + element + ''.join(letters[i + 1:])
            if inDict(new_word, dictionary):
                fix_word += new_word
                fixed = True
                break
        if fixed:
            break
        previous += letters[i]
    if fixed:
        return True, fix_word
    else:
        return False, ""


def fix_by_additional(dictionary, letters):
    """Spell checks to determine if an additional letter in any position forms a correct word"""
    previous = ""
    fix_word = ""
    fixed = False
    for i in range(len(letters)):
        # runs though the entire alphabet and adds it to the current position
        for alpha in ALPHABET:
            new_word = previous + alpha + ''.join(letters[i:])
            if inDict(new_word, dictionary):
                fix_word += new_word
                fixed = True
                break
        if fixed:
            break
        previous += letters[i]
    if fixed:
        return True, fix_word
    else:
        return False, ""


def fix_by_removal(dictionary, letters):
    """Spell checks to see if the removing a letter makes a correct word"""
    previous = ""
    fix_word = ""
    fixed = False
    for i in range(len(letters)):
        new_word = previous + ''.join(letters[i + 1:])
        if inDict(new_word, dictionary):
            fix_word += new_word
            fixed = True
            break
        previous += letters[i]
    if fixed:
        return True, fix_word
    else:
        return False, ""


def process_letters(word, dictionary, adj_letters):
    """Runs each of the spell checkers, and determines if any are true.  If none are true returns the original word and
    returns False for saying the word was not fixed"""
    letters = []
    for letter in word:
        letters += letter
    fixed, fix_word = fix_by_adjacent(dictionary, adj_letters, letters)
    if fixed:
        return fixed, fix_word
    fixed, fix_word = fix_by_additional(dictionary, letters)
    if fixed:
        return fixed, fix_word
    fixed, fix_word = fix_by_removal(dictionary, letters)
    if fixed:
        return fixed, fix_word
    else:
        return False, word


def inDict(word, dictionary):
    """Runs through the English dictionary to see if the word is a legal word"""
    for element in dictionary[word[0]]:
        if element == word:
            return True


def swap(lst, i, j):
    """Swaps I for J"""
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    return lst


def get_word(word):
    """Gets the word from the split string from the punctuation"""
    punctuation_word = pu.process_punctuation(word)
    w = punctuation_word[math.floor(len(punctuation_word) / 2)]
    for punct in pu.PUNCTUATION:
        if w == punct:
            return punctuation_word[0], punctuation_word
    return w, punctuation_word

