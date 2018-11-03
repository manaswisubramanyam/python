no=[]
even_sum=0
odd_sum=0
n=int(input("enter number of list elements"))
for x in range(1,n+1):
    value=int(input("enter %d element:" %x))
    no.append(value)
for j in no:
    if(j%2==0):
        even_sum=even_sum+1
    else:
        odd_sum=odd_sum+1
print("number of even numbers",even_sum)
print("number of odd numbers",odd_sum)