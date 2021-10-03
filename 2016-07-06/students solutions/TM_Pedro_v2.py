#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tm(seq):
    seq=seq.upper()
    r=0
    for i in seq:
        if i=="A":
            r=r+2
        elif i=="T":
            r=r+2
        elif i=="C":
            r=r+4
        elif i=="G":
            r=r+4
        else:
            return "Nucleotide error"
    return r



if __name__ is "__main__":
    seq=raw_input("What is your sequence? ")
    print "TM is", tm(seq),"ºC"
