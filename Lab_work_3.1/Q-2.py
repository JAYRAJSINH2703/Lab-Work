a=int(input("Enter Any Number :"))
b=int(input("Enter Any Number :"))
c=int(input("Enter Any Number :"))
d=int(input("Enter Any Number :"))




if (a>b and a>c and a>d):
    print("A is Maximum")
elif(b>a and b>c and b>d):
    print("B is Maximum")
elif (c>a and c>b and c>d):
    print("C is Maximum")
else:
    print("D is Maximum")