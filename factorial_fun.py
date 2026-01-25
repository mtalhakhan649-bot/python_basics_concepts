#write a program to print the factorail of the number using funtion

def factoraal(n):
    if(n==1 or n==0):
        return 1
    return n * factoraal(n-1) 
n=int(input("enter your number"))
print(f"the factorial of the number  :{factoraal(n)}")#funtion call