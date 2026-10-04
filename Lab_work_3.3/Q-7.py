# A 
# B A
# C B A 
# D C B A
# E D B C A


for i in range (65,70):
    for j in range(i,64,-1):
        print(chr(j),end=" ")
    print()