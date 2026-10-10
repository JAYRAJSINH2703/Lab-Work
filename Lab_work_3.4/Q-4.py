# 1 0 1 0 1
#   0 1 0 1 
#     1 0 1
#       0 1
#         1 

for i in range(5,0,-1):
    for s in range(5-i):
        print(" ",end=" ")
    for j in range(5-i,5):
        if j%2 == 0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
