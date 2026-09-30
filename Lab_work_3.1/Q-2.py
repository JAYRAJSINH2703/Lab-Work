a=int(input("Enter Any Number :"))
b=int(input("Enter Any Number :"))
c=int(input("Enter Any Number :"))
d=int(input("Enter Any Number :"))





if a>b:
    if a>c:
        if a>d:
            print(a,"is largest number")
        else:
            print(d,"is the largest number")
    else:
        if c>d:
            print(c,"is the largest")
        else:
            print(d,"is the largest")   

else:
    if b>c:
        if b>d:
            print(b,"is the largest number")
        else:
            print(d,"is the largest number")
    else:
        if c>d:
            print(c,"is the largest")
        else:
            print(d,"is the largest")            


