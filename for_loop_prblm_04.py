#searching through for loop
tup=("shah",234,"ahamd",324,"talha",6453)
x=input("enter searching element:")
indx=0
for sr in tup:
    if sr==x:
        print("element found :",indx)
        break
        print(sr)
    else:
        print("not")
    indx+=1
    
   