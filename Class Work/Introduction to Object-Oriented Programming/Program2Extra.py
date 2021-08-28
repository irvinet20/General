dna = input("Enter a DNA sequence: ")
pattern = input("Enter the pattern: ")
rpattern = pattern[::-1]

dnaP = dna.split(pattern)
prefix = dnaP[0]
dna2 = dnaP[1]
dnaRP = dna2.split(rpattern)
middle = dnaRP[0]
rmiddle = middle[::-1]
suffix = dnaRP[1]

print("Prefix:", prefix)
print("Marker:", pattern)
print("Middle:", middle)
print("Reversed Middle:", rmiddle)
print("Reversed Marker:", rpattern)
print("Suffix:", suffix)
print("Result:", prefix+pattern+rmiddle+rpattern+suffix)
