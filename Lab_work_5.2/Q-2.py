person={
    "Name":"Alice",
    "Age":23,
    "city":"New York"
}

print("person ", person)


# Adding

person["MobileNumer"]=925292552

print(f"After Adding Number {person}")


# Updating

person["Age"]=18

print(f"After Updating the Age{person}")

# Removeing

del person["city"]

print(f"After removing the one value{person}")