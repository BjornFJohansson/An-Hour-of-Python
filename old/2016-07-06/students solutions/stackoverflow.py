

# http://stackoverflow.com/questions/19570800/reverse-complement-dna

def complement(s):
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    #letters = list(s)
    letters = [basecomplement[base] for base in s]
    return ''.join(letters)
def revcom(s):
    complement(s[::-1])

print("ACGTAAA")
print(complement("ACGTAAA"[::-1]))
print(revcom("ACGTAAA"))
