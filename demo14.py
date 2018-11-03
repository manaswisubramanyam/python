n=[]
no=int(input("enter 4digit number"))
res=0
while(no!=0):
    r=no%10
    res=res*10+r
    no=no//10
print("reverse number",res)