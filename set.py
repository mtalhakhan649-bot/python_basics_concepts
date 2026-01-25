s1=set()#emty set 
print(type(s1))
print(s1.add(1))
print(s1.add(2))
print(s1.add((True)))#boolean in set
print(s1.add(584.458))#floating points in set
print(s1.add(("first",1,"secnd",2)))#tuple in set
print(s1.add(2))
print(s1.add("khan"))#string in set
# print(s1.add(["jioafhe",8347]))#list are not allowd in set bzc list are mutibl
print(s1)


s2={3,65,76,"khan","khan""yousafzai",45,87}
# print(s2[0])#not possible in  set 
print(len(s2))
print(s2)