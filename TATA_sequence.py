#Brendan Hendricks
#TATA

import re
import sys

motif = r'TATA(AA|AT)'


if len(sys.argv) == 1:
    print('Please provide a command line argument as a file name!')
    sys.exit()
else:
    myfile = sys.argv[1]
 
sequence = ''
 
try:
    with open(myfile, 'r') as f:
        for line in f:
            if '>' not in line:
                sequence = sequence + line.strip()
except OSError as oserr:
    print('OS error:', oserr)
else:
    print(sequence)

try:
    re.compile(motif)
except:
    print('Invalid regular expression, exiting the program!')
    sys.exit()


matches = re.finditer(motif,sequence)

if matches:
    for match in matches:
        print(match, "Start index:",match.start(0),"Final index:",match.end(0))

else:
   print("There are no TATA boxes")
