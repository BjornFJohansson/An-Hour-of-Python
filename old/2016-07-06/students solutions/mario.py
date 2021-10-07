def complement(watson):
    watson=watson.lower()
    r=""
    for i in watson:
        if i=="a":
            r=r+"t"

        elif i=="t":
            r=r+"a"

        elif i=="c":
            r=r+"g"

        elif i=="g":
            r=r+"c"

        else:
           r=r+"?"
    return r

print complement("GGATCC")

