#Brendan Hendricks
#April 17, 2023
#HW 10 EX 4.3

x = [0] * 13
r  = 3.73
x[0] = 0.43
n = 0


while(n<12):
    x[n+1] = r * x[n] * (1.0 - x[n])
    print("Generation",n+1, "has a population density of:",x[n+1])
    n =  n+1

                         


    
