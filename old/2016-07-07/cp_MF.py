# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 09:28:47 2016

@author: mariscuba
"""

def cloning_primer(seq, L):
    seq=seq.lower()
    print "my_sequence is:", seq
    print "forward_primer is:", seq[:L]
    n=""
    for i in seq:
       if i=="a":
          n="a"+n
       elif i=="t":
          n="t"+n
       elif i=="g":
          n="g"+n
       elif i=="c":
          n="c"+n
       else:
          n=n+"?"
    print "reverse_primer is:", n[:L]
    return ""

print cloning_primer("atgctcgatcgctaaattcgtatgctg", 5)


