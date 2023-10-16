#Brendan Hendricks
#April 9, 2023
#Hw9 Ex 3.2

BRAC2 = "gggtgcgacg attcattgtt ttcggacaag tggataggca accactaccg gtggattgtc"

first = BRAC2[0:3]
second = BRAC2[3:6]
third = BRAC2[6:9]
third_to_last = BRAC2[-9:-6]
second_to_last = BRAC2[-6:-3]
last = BRAC2[-3:]

print("First 3 codons:",first,second,third)
print("Last 3 codons:",third_to_last,second_to_last,last)
