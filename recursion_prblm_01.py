def cal(n):
    if(n==0):
        return 0
    return(n-1)+n

sum=cal(int(input("enter value:")))
print(cal(sum))
