#Brendan Hendricks
#April 21, 2023
#HW11 EX 6.6

import sys
import os.path
 
if len(sys.argv) == 1 or  len(sys.argv) == 2:
   print('Please provide 2 command line arguments')
   sys.exit()
else:
   myfile1 = sys.argv[1]
   myfile2 = sys.argv[2]

try:
    f = open(myfile1, "r")
    g = open(myfile2, "w")
except OSError as oserr:
    print('OS error:', oserr)
else:
    for line in f:
       g.write(line)
