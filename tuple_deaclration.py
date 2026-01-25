tup=(1,)#singlton tuple which have only one argument
print(type(tup))
print(tup)
tup2=()#emty tuple
print(type(tup2))
print(tup2)
#immutibility
tup3=(2,3,4,5)
print(tup3[1])#3
print(tup3[0])#2
tup3[0]=9#does not chang bzc tuple are immutiblle
print(tup3)
