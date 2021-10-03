# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 14:19:46 2016

@author: Master
"""

def rc (my_seq):
    mydict = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
    return "".join([mydict[base] for base in reversed(my_seq)])

print rc("GGTAC")










