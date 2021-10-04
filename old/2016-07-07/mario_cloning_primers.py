def cloning_primers(seq, L):
    seq=seq.lower()
    f=""
    r=""
    for i in seq:
        if i=="a":
            r=r+"t"
            f=f+"a"
        elif i=="t":
            r=r+"a"
            f=f+"t"
        elif i=="c":
            r=r+"g"
            f=f+"c"
        elif i=="g":
            r=r+"c"
            f=f+"g"
        elif i=="n":
            r=r+"n"
            f=f+"n"
        else:
            r=r+"?"
            f=f+"?"
    print "Primer forward is: ", f[:L]
    print "Primer reverse is: ", r[:(-L-1):-1]
    return ""

if __name__ is "__main__":
    seq=raw_input("what is your sequence? ")
    L=input("what is the lengh? ")
    print cloning_primers(seq, L)