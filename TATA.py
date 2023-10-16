#Brendan Hendricks
#TATA

import re
import sys



DNA_sequence = "AGTTGTTGATCTGTGTGAGTTATAAACAGACTGCGACAGTTCGTATAATAGTCTGAAGCGAGAGCTAACAACAGTATCAACA"

motif = r'TATA(AA|AT)'


try:
    re.compile(motif)
except:
    print('Invalid regular expression, exiting the program!')
    sys.exit()


matches = re.finditer(motif,DNA_sequence)

if matches:
    for match in matches:
        print(match, match.start(0), match.end(0))

else:
   print("There are no TATA boxes")
