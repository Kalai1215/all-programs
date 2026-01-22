i=20
sum=0
while i>=11:
    if i%2==0:
        print(i,end="-")
        sum+=i
        i-=1
    elif (i%2==1 and i!=11):
        print(i,end="+")
        sum-=i
        i-=1
    else:
        print(i, end="=")
        sum-=i
        i-=1
print(sum)
