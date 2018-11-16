"""
    File: punctuation_process.py
    Author: Nicholas Curl
    Description: project
"""

import re
import math
import string

# Global variable for the punctuation
PUNCTUATION = list(string.punctuation)


def process_punctuation(word):
    """Splits the string based on punctuation except for ' and _"""
    word = word.strip()
    return re.split("([^'a-zA-Z0-9_])", word)


def apply_punctuation(punctuation_word, word):
    """Reapplies the punctuation to the word"""
    w = punctuation_word[math.floor(len(punctuation_word) / 2)]
    isPunct = False
    for punct in PUNCTUATION:
        if w == punct:
            isPunct = True
            break
    if isPunct:
        punctuation_word[0] = word
    else:
        punctuation_word[math.floor(len(punctuation_word) / 2)] = word
    return ''.join(punctuation_word)
