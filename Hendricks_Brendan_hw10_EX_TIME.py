#Brendan Hendricks
#April 18, 2023
#HW10 EX TIME
import time
 
DNA_seq = 'CGGACACACAAAAAGAATGAAGGATTTTGAATCTTTATTGTGTGCGAGTAACTACGAGGAAGATTAAAGA'
N = 10000
#The larger the value of N, the greater the ratio of while time / .count
#time will be
DNA_seq = DNA_seq * N
print('DNA sequence:', DNA_seq)
 
bp = 'T'
print('Base pair:', bp)
t1 = time.process_time()
print('str.count():', DNA_seq.count(bp))
t2 = time.process_time()
runtime1 = t2-t1
print("Time taken for method:",runtime1)
 
count = 0
index = 0
t3 = time.process_time()
while index < len(DNA_seq):
    if bp == DNA_seq[index]:
        count += 1
    index += 1
    
t4 = time.process_time()
runtime2 = t4 - t3
print('Our while count:', count)
print("Time taken for method:",runtime2)


print("Runtime ratio of while loop over .count method:", runtime2/runtime1)
#Running my code several times, the ratio can change slightly but mostly stays
#in the same range.

#Using the time.process_time() method and the time.time() method
#yield very similar results in the ratio of while time / .count time
