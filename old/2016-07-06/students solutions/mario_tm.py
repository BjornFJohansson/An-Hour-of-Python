def tm(seq):
    seq=seq.lower()
    a=0
    t=0
    c=0
    g=0
    for i in seq:
        if i=="a":
            a=a+1
        elif i=="t":
            t=t+1
        elif i=="c":
            c=c+1
        elif i=="g":
            g=g+1

    mt=(4*g)+(4*c)+(2*a)+(2*t)

    return mt

print tm("aaaaggggtgtgagaatga")

