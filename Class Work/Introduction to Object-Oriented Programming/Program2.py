dna = input("Enter a DNA sequence: ")
pattern = input("Enter the pattern: ")
rpattern = pattern[::-1]
if dna.find(pattern) == -1 or dna.find(rpattern) == -1:
  print('Invalid Entry')
else:
  dnas = dna[dna.index(pattern)+len(pattern):] #dnas for dna split, used incase of a reverse of the pattern appearing before the first occurance of the pattern 
  prefix = dna[0:dna.index(pattern)]
  rpattern = pattern[::-1]
  middle = dnas[:dnas.index(rpattern)]
  rmiddle = middle[::-1]
  suffix = dnas[dnas.index(rpattern)+len(rpattern):]

  print("Prefix:", prefix)
  print("Marker:", pattern)
  print("Middle:", middle)
  print("Reversed Middle:", rmiddle)
  print("Reversed Marker:", rpattern)
  print("Suffix:", suffix)
  print("Result:", prefix+pattern+rmiddle+rpattern+suffix)
