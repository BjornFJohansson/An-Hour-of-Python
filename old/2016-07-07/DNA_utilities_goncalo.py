#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 08:20:35 2016

@author: Gonçalo
"""

def complement(seq):
   ns=""
   for i in seq:
        if i=="a":
            ns=ns+"t"
        elif i=="t":
            ns=ns+"a"
        elif i=="c":
            ns=ns+"g"
        elif i=="g":
            ns=ns+"c"
        elif i=="A":
            ns=ns+"T"
        elif i=="T":
            ns=ns+"A"
        elif i=="C":
            ns=ns+"G"
        elif i=="G":
            ns=ns+"C"
   return ns

def complement_reverse(seq):
   comp=complement(seq)
   rc = comp[::-1]
   return rc


if __name__ is "__main__":
    seq = raw_input('What is your seq?')
    print 'Complement- ' + complement(seq)
    print'Complement reverse- ' + complement_reverse(seq)