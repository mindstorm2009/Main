"""
    File: words.py
    Author: Nicholas Curl
    Description: project
"""

import spell_checker as sp
import capitalization_process as caps
import punctuation_process as pu
import input_read as rd


def words(args, dictionary, letters):
    """The function that runs the spell checker and outputs the incorrect words and its change to the correct words"""
    words_read = 0
    unknown = []
    incorrect = []
    # Reads the input
    line_list = rd.read_input(args)
    # Runs through the words by line
    for i in range(len(line_list)):
        word_list = line_list[i]
        # Runs through the words in the current line
        for word in word_list:
            words_read += 1
            # Strips the punctuation
            w, punctuation_word = sp.get_word(word)
            # Converts the word to lowercase if the capitalized word is not in the dictionary
            new_word, isCapital = caps.process_capital(w, dictionary)
            # Checks to see if the lowercase word is in the dictionary, if it is moves to the next word
            if not sp.inDict(new_word, dictionary):
                incorrect += [word]
                # Runs the spell checker
                fixed, fix_word = sp.process_letters(new_word, dictionary, letters)
                # Checks to see if the word is fixed if it is not adds the word to the unknown word list
                if not fixed:
                    incorrect.remove(word)
                    unknown += [fix_word]
                    continue
                # Checks to see if the original word was capitalized if it was reapplies the capitalization
                if isCapital:
                    fix_word = fix_word[0].upper() + fix_word[1:]
                # Reapplies the punctuation
                fix_word = pu.apply_punctuation(punctuation_word, fix_word)
                print(word, "->", fix_word)
    print("\n", words_read, " words read from file", sep="")
    if len(incorrect) > 0:
        print("\n", len(incorrect), " Corrected Words", sep="")
        print(incorrect, "\n")
    if len(unknown) > 0:
        print(len(unknown), "Unknown Words")
        print(unknown)

