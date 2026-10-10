Name = input("enter your name:")


print(f"entered name:{Name}")


palindrome = Name[::-1]


if palindrome == Name:
    print("given name is palindrome")
else:
    print("given name is not palindrome")