#Brendan Hendricks
#April 20, 2023
#HW11 6.1

import sys

if len(sys.argv) ==1:
    print("Command line argument needed")
    sys.exit()
else:
    myfile = sys.argv[1]
sequence = ""
try:
    with open(myfile,"r") as f:
        for line in f:
            if ">" not in line:
                sequence = sequence + line.strip()
except OSError as oserr:
    print("OS error:",oserr)
else:  
    print(sequence)
    print("bps:",len(sequence))
