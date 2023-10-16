#Brendan Hendricks
#RE Substitution

import re

dna = "601 accacac gacgag gtattag"
dna1 = re.sub(r"[\d\s]", "", dna)
print(dna1)

dna2 = re.subn('a', 'a', dna1)
print(dna2)
print(dna2[1])
