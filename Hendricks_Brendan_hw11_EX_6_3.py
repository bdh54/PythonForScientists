#Brendan Hendricks
#April 20, 2023
#HW11 EX 6.3

import sys

if len(sys.argv) ==1:
    print("Command line argument needed")
    sys.exit()
else:
    myfile1 = sys.argv[1]
sequence = ""
try:
    with open(myfile1,"r") as f:
        for line in f:
            if ">" not in line:
                sequence = sequence + line.strip()
except OSError as oserr:
    print("OS error:",oserr)
else:  
    print(sequence)
    print("NEXT SEQUENCE")

myfile2 = sys.argv[2]
sequence2 = ""
try:
    with open(myfile2,"r") as f:
        for line in f:
            if ">" not in line:
                sequence2 = sequence2 + line.strip()
except OSError as oserr:
    print("OS error:",oserr)
else:  
    print(sequence2)
    
for i in range(len(sequence2)-1):
    if (sequence2[i] != sequence[i]):
        print("There is a difference at indecies:",i)
    
    
