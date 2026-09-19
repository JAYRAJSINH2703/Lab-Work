a=int(input("Enter Any Number :"))
b=int(input("Enter Any Number :"))

c=input("Take any Operator :")

d=a+b

e=a*b

f=a/b

g=a-b


if (c=='+'):
    print("You Enter + ,So Addition is :",d)
elif(c=='-'):
    print("You Enter -,So Substraction is :",g)
elif(c=='*'):
    print("You Enter *,So Muliplication is:",e)
else:
    print("You Enter,So Division is :",f)