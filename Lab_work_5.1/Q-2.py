Numberlist=int(input("how many numbers do you want to enter :"))

Num=[]


for i in range (Numberlist):
    num=int(input(f"enter number {i+1}:"))

    Num.append(num)


maxNumberlist=min(Num)

minNumberlist=max(Num)


print("max number", maxNumberlist)

print("min number", minNumberlist)