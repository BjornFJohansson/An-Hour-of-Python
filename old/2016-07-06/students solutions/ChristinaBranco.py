def tm(seq):
    q = 0
    for i in seq:
        if i == "A" or i == "T":
            q=q+2
        elif i == "G" or i == "C":
            q=q+4
    return q

print tm("GCTTT")