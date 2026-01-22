a=[10,30,40,50]
print(a)
value=int(input('enter the value to be inserted:'))
n=int(input('enter the index where value is to be inserted:'))
a.append('none')
for i in range(len(a)-1,n,-1):
    a[i]=a[i-1]
a[n]=value
print(a)
