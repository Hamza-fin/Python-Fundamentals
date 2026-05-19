mylist = ["the","quick","brown","fox"]

# Membership operators
print("quick" in mylist)
print("quick" not in mylist )

# List  slicing using index

sublist = mylist[0:3]
print(f"{sublist=}")

restlist = mylist[2:]
print(restlist)

leftlist = mylist[:3]
print(leftlist)

#Indexing from the end. End not included

endlist1 = mylist[-3:-0]
print(f"{endlist1=}")

endlist = mylist[-3:]
print(endlist)

#List concatenation

newlist = mylist + mylist
print(newlist)