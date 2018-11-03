no=int(input("enter number"))
sum=0
while(no!=0):
    r=no%10
    no=no//10
    sum+=r
print("sum of given no",sum)