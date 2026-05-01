#List creation

alist = [1,"Fox",3]         #Defined list
blist = list((1,'Fox',3))   #List from tuple using constructor
clist = list()              #Empty list
print(f"{alist = }")
print(f"{blist = }")
print(f"{clist = }")

#Duplicate elements allowed
dlist = [1,1,2,3]
print(f"{dlist = }")