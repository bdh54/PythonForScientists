#Brendan Hendricks
#April 20, 2023
#HW11 5.7

from dna_rna import *

zyka_DNA = "GGTCCACCCATGAGAGAGATCATACTCAAGGTGGTCCTGATGGCCATCTGTGGCATGAACCCAATAGCTA"

zyka_RNA = DNAtoRNA(zyka_DNA)
print("Zyka RNA:", zyka_RNA)

zyka_DNA_Conversion = RNAtoDNA(zyka_RNA)
print("Zyka DNA:", zyka_DNA_Conversion)

if(zyka_DNA == zyka_DNA_Conversion):
    print("Matches Original: TRUE")
else:
    print("Matches Original: FALSE")

