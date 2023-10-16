#Brendan Hendricks
#April 17, 2023
#HW EX 4.8

import random

DNA = ""
a_counter = 0
c_counter = 0
g_counter = 0
t_counter = 0

chars =["A","C","G","T"]

for c in range(1001):
    index = random.randint(0,3)
    DNA += chars[index]

print("DNA:",DNA)
for c in DNA:
    if c == 'A':
        a_counter += 1
    if c == 'C':
        c_counter += 1
    if c == 'G':
        g_counter += 1
    if c==  'T':
        t_counter += 1


print("Percentage of 'A' that appears in DNA:", a_counter/len(DNA) * 100,"\b%")
print("Percentage of 'C' that appears in DNA:", c_counter/len(DNA) * 100,"\b%")
print("Percentage of 'G' that appears in DNA:", g_counter/len(DNA) * 100,"\b%")
print("Percentage of 'T' that appears in DNA:", t_counter/len(DNA) * 100,"\b%")
