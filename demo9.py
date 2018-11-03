no=int(input("enter number"))
if no>1:
    for x in range(2,no):
        if(no%x)==0:
            print("number is not prime")
            break
    else:
        print("number is prime")
else:
    print("number is not prime")