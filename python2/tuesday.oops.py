p=0
for i in range(1,6):
    p=i*i-p
    k=p
    for j in range(i):
        print(k,end=' ')
        k-=1
    print()

'''def fibonacci_helper(n,r=[]):
    for i in range(n+1):
        if i==0:
            r.append(0)
        elif i==1:
            r.append(1)
        else:
            x=r[i-1]+r[i-2]
            r.append(x)
    return(r[n])
def fibonacci(a):
    print(fibonacci_helper(a))
fibonacci(10)'''

a=['bala','kalai','apple']
c=[]
for i in a:
    k=list(i)
    for j in range(len(k)):
        for l in range(j,len(k)):
            if k[j]>k[l]:     #k[j]<k[l]
                temp=k[j]
                k[j]=k[l]
                k[l]=temp
    c.append(''.join(k))
print(c)
