#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eduardo Silva
seq=raw_input('Enter your sequence-->')
def tm(seq):
    ns=0
    for i in seq:
        if i=="A" or i=="T":
         ns=ns+2
        elif i=="G" or i=="C":
         ns=ns+4
    return ns


print tm(seq),"ºC"



