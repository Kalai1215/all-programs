unit=int(input("Enter the unit:"))
fixedcharge=100
if unit<1:
    amount="No bill"
elif 1<unit<101:
    amount=fixedcharge
elif 100<unit<201:
    amount=((100-0)*1)+((unit-100)*2)+ fixedcharge
elif 200<unit<301:
    amount=((100-0)*1)+((200-100)*2)+((unit-200)*3)+ fixedcharge
else:
    amount="unit exceeded"
print("Bill amount",amount)

n=int(input("enter the rows:"))
space=n-1
for i in range(0,n+1):
    for j in range(0,space):
        print(end=" ")
    space-=1
    for j in range(0,i+1)
        

