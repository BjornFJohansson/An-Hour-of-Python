
def complement(x):
    x=x.upper()
    bases={"A":"T", "T":"A", "C":"G", "G":"C"}
    #complement = [bases[y] for y in x]
    rc=""
    for i in x:
        rc=rc+bases[i]

    return rc

print complement("ggataa")

