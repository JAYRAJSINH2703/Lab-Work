text=input("Enter Any Text :")

for ch in text:
    if ch in "AEIOU,aeiou":
        continue
    print(ch)