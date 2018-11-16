"""
    File: capitalization_process.py
    Author: Nicholas Curl
    Description: project
"""

import spell_checker


def process_capital(word, dictionary):
    """Checks to see if the capitalized word is in the dictionary if it is not returns the lowercase version of the
    word"""
    if not spell_checker.inDict(word, dictionary):
        if word[0].isupper():
            new_word = word[0].lower() + word[1:]
            return new_word, True
        else:
            return word, False
    else:
        return word, True
