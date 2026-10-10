list=([1,2],[3,4],[5,6])

print(list)


list[1].append(9)

print(f"After Adding Value {list}")


# why its happening ?

# Tuple is imutable but his value is containing list vlaue wich are mutable.