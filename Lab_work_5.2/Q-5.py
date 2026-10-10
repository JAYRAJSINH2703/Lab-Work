num=int(input("Enter the that you want to enter Number :"))

numlist=[]

for i in range(num):

    num=int(input(f"Enter the number {i+1}:"))

    numlist.append(num)


print(f"Number list {numlist}",type(numlist))


numlist=set(numlist)

print(numlist,type(numlist))


numlist=tuple(numlist)

print(numlist,type(numlist))



