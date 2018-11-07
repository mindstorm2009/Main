"""
    File: dna.py
    Author: Nicholas Curl
    Description: lab

"""

from dataclasses import dataclass
from typing import Any, Union
import linked_code as lc


@dataclass(frozen=True)
class DNA:
    __slots__ = 'value', 'rest'
    value: Any
    rest: Union[None, 'DNA']


def convert_to_nodes(dna_string):
    """Converts the inputted string to a node structure"""
    if dna_string == "":
        return None
    else:
        return DNA(dna_string[0], convert_to_nodes(dna_string[1:]))


def convert_to_string(dna_seq):
    """Takes an inputted node sequence and converts it to a string"""
    if dna_seq is None:
        return ""
    else:
        dna_string = dna_seq.value + convert_to_string(dna_seq.rest)
        return dna_string


def is_match(dna_seq1, dna_seq2):
    """Checks to see if both of the DNA sequences are the same"""
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    elif dna_seq1.value == dna_seq2.value:
        return is_match(dna_seq1.rest, dna_seq2.rest)
    else:
        return False


def is_pairing(dna_seq1, dna_seq2):
    """Checks to see if the inputted DNA sequences are pairs to each other, i.e., A matches with T and G matches with C
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    elif dna_seq1.value == "A" and dna_seq2.value == "T":
        return is_pairing(dna_seq1.rest, dna_seq2.rest)
    elif dna_seq1.value == "T" and dna_seq2.value == "A":
        return is_pairing(dna_seq1.rest, dna_seq2.rest)
    elif dna_seq1.value == "G" and dna_seq2.value == "C":
        return is_pairing(dna_seq1.rest, dna_seq2.rest)
    elif dna_seq1.value == "C" and dna_seq2.value == "G":
        return is_pairing(dna_seq1.rest, dna_seq2.rest)
    else:
        return False


def is_palindrome(dna_seq):
    """Checks to see if the sequence is a palindrome"""
    if dna_seq is None or dna_seq.rest is None:
        return True
    elif dna_seq.value == lc.reverse_iter(dna_seq).value:
        dna_seq = lc.remove_at(lc.length_iter(dna_seq) - 1, dna_seq)
        return is_palindrome(dna_seq.rest)
    else:
        return False


def substitution(dna_seq1, idx, base):
    """substitutes the allele at the given index with base"""
    if idx > lc.length_iter(dna_seq1) - 1:
        raise IndexError("Index out of range")
    elif idx == 0:
        return DNA(base, dna_seq1.rest)
    else:
        return DNA(dna_seq1.value, substitution(dna_seq1.rest, idx - 1, base))


def insertion(dna_seq1, dna_seq2, idx):
    """Inserts a second DNA sequence in the first sequence at a given index"""
    if idx > lc.length_iter(dna_seq1):
        raise IndexError("Index out of range")
    elif idx == 0:
        return lc.concatenate(dna_seq2, dna_seq1)
    else:
        return DNA(dna_seq1.value, insertion(dna_seq1.rest, dna_seq2, idx - 1))


def deletion(dna_seq, idx, segment_size):
    """Deletes a segment from the sequence starting at the index and going till it reaches segment_size"""
    if segment_size == 0:
        return dna_seq
    elif idx > lc.length_iter(dna_seq) or idx + segment_size > lc.length_iter(dna_seq):
        raise IndexError("Index out of range")
    elif idx == 0:
        if segment_size == 0:
            return dna_seq.rest
        else:
            return deletion(dna_seq.rest, idx, segment_size - 1)
    else:
        return DNA(dna_seq.value, deletion(dna_seq.rest, idx - 1, segment_size))


def duplication(dna_seq, idx, segment_size):
    """Duplicates a segment in the sequence starting at the index and going to it reaches segment_size and places it
    after the the duplicated segment"""
    if segment_size == 0:
        return dna_seq
    elif idx > lc.length_iter(dna_seq) or idx + segment_size > lc.length_iter(dna_seq):
        raise IndexError("Index out of range")
    elif idx == 0:
        if segment_size == 0:
            return
        else:
            return DNA(dna_seq.value,
                       lc.insert_at(segment_size - 1, dna_seq.value, duplication(dna_seq.rest, idx, segment_size - 1)))
    else:
        return DNA(dna_seq.value, duplication(dna_seq.rest, idx - 1, segment_size))
