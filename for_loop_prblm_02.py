#find weather the number prime or not
no=int(input("entr no  :"))
for i in range(2,no):
    if(no%i)==0:
        print('number is not prime ')
        break
else:
    print("numbr is prime")