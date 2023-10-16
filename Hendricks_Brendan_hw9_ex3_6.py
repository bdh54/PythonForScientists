#Brendan Hendricks
#April 9, 2023
#Hw9 3.6

BRAC2 = "gggtgcgacgattcattgttttcggacaagtggataggcaaccactaccggtggattgtc"
a_counter = 0
c_counter = 0
g_counter = 0
t_counter = 0
for c in BRAC2:
    if c == 'a':
        a_counter += 1
    if c == 'c':
        c_counter += 1
    if c == 'g':
        g_counter += 1
    if c==  't':
        t_counter += 1

print("Percentage of 'a' that appears in BRAC2:", a_counter/len(BRAC2) * 100,"\b%")
print("Percentage of 'c' that appears in BRAC2:", c_counter/len(BRAC2) * 100,"\b%")
print("Percentage of 'g' that appears in BRAC2:", g_counter/len(BRAC2) * 100,"\b%")
print("Percentage of 't' that appears in BRAC2:", t_counter/len(BRAC2) * 100,"\b%")



        
