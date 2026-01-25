'''list:- builtin data type which is mutible
it is just like array but in array we can store only
same datatype variables in this we can store multiple 
type varibles like string,floating point,integer etc'''


marks=["phy",98,"bio",94,"chem",93,"math",80,"urdu",91]
print(type(marks))
print(len(marks))
print(marks)
# mutibility
marks[1]="100"
print(marks)
