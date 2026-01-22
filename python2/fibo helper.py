'''p=0
for i in range(1,6):
    p=i*i-p
    k=p
    for j in range(i):
        print(k,end='',sep='')
        k-=1
    print()'''

def fibonacci_helper(n,r=[]):
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
fibonacci(10)
