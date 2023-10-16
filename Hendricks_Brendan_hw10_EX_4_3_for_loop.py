#Brendan Hendricks
#April 17, 2023
#HW EX 4.3 (for loop)

r = 3.73
x=[0] * 13
x[0] = 0.43
n = 0

for n in range (0,12):
    x[n+1] = r * x[n] * (1.0 - x[n])
    print("Generation",n+1,"hasa population density of:",x[n+1])

