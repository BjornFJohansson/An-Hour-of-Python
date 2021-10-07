def tm(seq):

    seq = seq.upper()

    ab = seq.count("A")
    tb = seq.count("T")
    cb = seq.count("C")
    gb = seq.count("G")

    t = ((ab*2)+(tb*2)+(cb*4)+(gb*4))

    return t


print tm("AAAAA")


