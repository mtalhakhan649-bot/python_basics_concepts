#WAP to search element in tuple through while loop

tup=("khan","shaheen","ahmad","yousafzai")
x=input("enter element to be search:")
i=0
while i<len(tup):
    if(tup[i]==x):
      print("element found at index:",i)
      break
    else:
        print("finding....")
    i+=1
print("END OF LOOP")

   