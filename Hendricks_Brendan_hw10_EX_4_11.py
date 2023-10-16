#Brendan Hendricks
#April 18, 2023
#HW 10 EX 4.11

import random

DNAseq = "GGCGATGCTAGTCGCGTAGTCTAAGCTGTCGAGAATTCGGATGTCATGA"

chars =  ["A","C","G","T"]
index1 = random.randint(0,48)

operation1 = random.randint(0,2)

if (operation1 == 0):
    index_for_chars = random.randint(0,3)
    DNAseq.replace(DNAseq[index1],chars[index_for_chars],1)
    print("Replacing")
if (operation1 == 1):
    index_for_chars = random.randint(0,3)
    DNAseq = DNAseq[:index1] + chars[index_for_chars] + DNAseq[index1:]
    print("Inserting")
if (operation1 == 2):
    DNAseq = DNAseq.replace(DNAseq[index1],"",1)
    print("Deleting")

index2 = random.randint(0,48)
operation2 = random.randint(0,2)

if (operation2 == 0):
    index_for_chars = random.randint(0,3)
    DNAseq.replace(DNAseq[index2],chars[index_for_chars],1)
    print("Replacing")
if (operation2 == 1):
    index_for_chars = random.randint(0,3)
    DNAseq = DNAseq[:index2] + chars[index_for_chars] + DNAseq[index2:]
    print("Inserting")
if (operation2 == 2):
    DNAseq = DNAseq.replace(DNAseq[index2],"",1)
    print("Deleting")


operation3 = random.randint(0,2)
index3 = random.randint(0,48)


if (operation3 == 0):
    index_for_chars = random.randint(0,3)
    DNAseq.replace(DNAseq[index3],chars[index_for_chars],1)
    print("Replacing")
if (operation3 == 1):
    index_for_chars = random.randint(0,3)
    DNAseq = DNAseq[:index3] + chars[index_for_chars] + DNAseq[index3:]
    print("Inserting")
if (operation3 == 2):
    DNAseq = DNAseq.replace(DNAseq[index3],"",1)
    print("Deleting")


print("Original String: GGCGATGCTAGTCGCGTAGTCTAAGCTGTCGAGAATTCGGATGTCATGA")
print("New String:      " + DNAseq)
    

