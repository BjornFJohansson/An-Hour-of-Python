#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 08:20:35 2016

@author: bjorn
"""

def complement(watson):
    ''' This function returns the complement strand of a DNA sequence.

    For example the sequence GGTAC should return CCTAG.

        GGTAC <- argument
        CCATG <- returned by function

    the argument is a string.

    compare with this online service:

    http://arep.med.harvard.edu/labgc/adnan/projects/Utilities/revcomp.html

    which has a function for complement strand

    This version should work for an argument containing ACG and T.

    look at this question and answers at stackoverflow:

    http://stackoverflow.com/questions/8848294/how-to-get-char-from-string-by-index


    string methods:
    https://docs.python.org/2/library/stdtypes.html#string-methods

    '''
    pass






def reverse_complement(watson):
    ''' This function returns the reverse complement strand of a DNA sequence.

    For example the sequence GGTAC should return CCTAG.

        GGTAC <- argument
        CCATG <- returned by function

    compare with this online service:

    http://arep.med.harvard.edu/labgc/adnan/projects/Utilities/revcomp.html

    which has a function for reverse complement strand

    This version should work for an argument containing ACG and T.

    look at this question and answers at stackoverflow:
    http://stackoverflow.com/questions/931092/reverse-a-string-in-python


    string methods:
    https://docs.python.org/2/library/stdtypes.html#string-methods

    '''

    pass


def tm(seq):
    ''' Tĥis function should return the melting temperature for a PCR primer.
    The PCR primer sequence is geven by the argument seq and can contain A,G,C and T

    The Wallace rule should be used:

    mp = 2°C(A+T) + 4°C(G+C)

    or

    mp = 4*numberofC + 4*numberofG +2*numberofA + 2*numberofT

    The function should return an integer corresponding to the melting
    temperature of the primer.

    tip!

    look at the selection of string methods here:
    https://docs.python.org/2/library/stdtypes.html#string-methods

    '''
    pass


def cloning_primers(seq, L):

    '''
    This function should return the forward and reverse primers.
    for the sequence seq of the length specified by L.

    seq is a tring, L is an integer.

    The function should return a list of strings
    representing the two primers as strings:

    [forward_primer, reverse_primer]

    The primers should be 5'-3'

    '''
    pass



if __name__ is "__main__":
    print complement("GGTAC")
    print reverse_complement("GGTAC")
    print tm("aaaaaaaaaa")

