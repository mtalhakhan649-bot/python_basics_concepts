def exam():
    a = int(input("enter marks of paper 1"))
    a1 = int(input("enter marks of paper 2 "))
    a2 = int(input("enter marks of paper 2 "))
    sum = a + a1 + a2
    print(f"the sum is {sum}")
    average = sum / 3
    print(f"the average is {average}")
    if average<50:
        print("fucked up")
    else:
        print("your are passeed ")



exam()#function call
print("than you")
exam()
print("than you")
