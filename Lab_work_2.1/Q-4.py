a=int(input("Enter Any Number :"))
b=int(input("Enter Any Number :"))
c=int(input("Enter Any Number :"))


if(a>b and a>c):
    print(a,"A is Maximun")
elif(c>a and c>b):
    print(c,"C is Maximum")    
else:
    print(b,"B is Maximum")