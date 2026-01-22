
b=[10,4,6,8,42,2,9,5,3,7,22]
for i in b:
    for j in range(2,i):
        
        if i%j==0:
            x=b[0]
            for i in b:
                if i<x:
                    x=i
            y=b[0]        
            for i in b:
                if i<y and i!=x:
                    y=i
            z=b[0]
            for i in b:
                if i<z and i!=x and i!=y:
                    z=i
print(x,y,z)
for i in b:
    for j in range(2,i):
        
        if i%j==0:
            x=b[0]
            for i in b:
                if i>x:
                    x=i
            y=b[0]        
            for i in b:
                if i>y and i!=x:
                    y=i
            z=b[0]
            for i in b:
                if i>z and i!=x and i!=y:
                    z=i
print(x,y,z)



        

number_of_inputs=int(input())
numbers=[]
def printBigThreeAndSmallThree(list1,num):
    x=[]
    for i in list1:
        for j in range(2,i):
            if i%j==0:
                x.append(i)
        for j in range(num):
            n=x[0]
            for i in x:
                if i<n:
                    n=i
            y=x[0]        
            for j in x:
                if j<y and j!=n:
                    y=j
            z=x[0]
            for k in x:
                if k<z and k!=n and k!=y:
                    z=k
            m=x[0]
            for f in x:
                if f>m:
                    m=f
            o=x[0]        
            for g in x:
                if g>o and g!=m:
                    o=g
            p=x[0]
            for h in x:
                if h>p and h!=o and h!=m:
                    p=h
    print(n,y,z)
    print(m,o,p)
for i in range(number_of_inputs):
    number=int(input())
    numbers.append(number)
printBigThreeAndSmallThree(numbers,number_of_inputs)

s=list((23,)*4)
print(s)

def fun(a=12,b=12):
    print(a//9)
    return (a*b)
print(fun(a=9,b=2))


f=[1,2,3]
f.clear()
print(f)


a=1
b=0
#print(any(a,b))
def fun():
    for i in range(22,23,24):
        print(i)
fun()

def x(values):
    values[0]=1
v=[2,3,4]
x(v)
print(v)

l=list("1234")
l[0]=l[1]=5
print(l)

