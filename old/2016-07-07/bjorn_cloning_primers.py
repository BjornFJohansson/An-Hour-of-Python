from DNA_utilities_goncalo import complement_reverse

def cloning_primers(seq, L):
    seq=seq.lower()
    f=""
    for i in seq:
        if i in ["a","g","c","t"]:
            f=f+i
        else:
            f=f+"?"
    return [ f[:L], complement_reverse(f[len(f)-L:]) ]


if __name__ is "__main__":

    seq=raw_input("what is your sequence? ")
    L=input("what is the lengh? ")

    f,p = cloning_primers(seq, L)

    print "Primer forward is: ", f
    print "Primer reverse is: ", p


