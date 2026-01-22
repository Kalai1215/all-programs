a=()
b=tuple()
print(type(a))
print(type(b))

print('----------------------------------------------')

a=('abcd',21,2.14,True)
print(a)

print('----------------------------------------------')

a=1,2,3,4,5,6,7
print(a)
b=33,
print(b)

print('----------------------------------------------')

a=(1,2,3,4)
b=list(a)
b.append(5)
a=tuple(b)
print(a)

print('----------------------------------------------')

a=('a','b','c','d')
b=''.join(a)
print(b)

print('----------------------------------------------')

a=(1,2,3,4,5,6,7,8,9,10,11,12)
print(a[3])
print(a[-4])

print('----------------------------------------------')

a=(1,2,3,4,'a','b',1,2)
b=[]
for i in a:
    if i in b:
        print(i)
    else:
        b.append(i)

print('----------------------------------------------')

a=(1,2,3,4,5,6)
n= int(input('enter a num:'))
if n in a:
    print('found')    #print(2 in a) True / False
else:
    print('not found')

print('----------------------------------------------')

a=[1,2,3,4]
b=tuple(a)
print(b)

print('----------------------------------------------')

a=(1,2,3,4)
b=[]
n=int(input('enter the num to be removed:'))
for i in a:           # list-->remove()
    if i==n:
        continue
    else:
        b.append(i)
c=tuple(b)
print(c)

print('----------------------------------------------')

a=(1,2,3,4,5,6)
print(a[:3])

print('----------------------------------------------')

a=(1,2,3,4)
b=a.index(2)
print(b)

print('----------------------------------------------')

a=(1,2,3,4,5)
print(len(a))

print('----------------------------------------------')

a=((1,2),(3,4),(5,6))
print(dict((i,j)for i,j in a))

print('----------------------------------------------')

a=(1,2,3,4,5)
b=[]
for i in range(-1,-len(a)-1,-1):
    b.append(a[i])
c=tuple(b)
print(c)

#a=(1,2,3,4,5)
#y=reversed(a)
#print(tuple(y))

#b=sorted(a)
#print(tuple(b))

print('----------------------------------------------')

a=[(1,2),(3,4),(5,6),(7,8)]
print(dict((i,j)for i,j in a))

print('----------------------------------------------')

a=(1,2,3)
print('tuple{}'.format(a))

print('----------------------------------------------')

'''list=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in list:
    i[-1]=100
print(list)'''

print('----------------------------------------------')

data= [(), ('',), ('a', 'b'),(), ('a', 'b', 'c'), ('d')]
for i in data:
    if i==():
        data.remove(())
    else:
        pass
print(data)

print('----------------------------------------------')

price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))

print('----------------------------------------------')

a=[1,2,3,(4,5),4]
x=0
for i in a:
    if type(i)== tuple:
        break
    else:
        x+=1
print(x)

print('----------------------------------------------')

s='string'
z=[]
for i in s:
    z.append(i)
c=tuple(z)
print(c)

print('----------------------------------------------')

a=(1,2,3,4)
b=1
for i in a:
    b*=i
print(b)

print('----------------------------------------------')

a=((1,2,3,4,5),(1,2,3),(4,5,6))
n=[]
for i in a:
    sum=0
    for j in range(0,len(i)):
        sum+=i[j]
    avg=sum/len(i)
    n.append(avg)
print(n)

print('----------------------------------------------')

a=(('333', '33'), ('1416', '55'))
b=[]
for i,j in a:
    b.append((int(i),int(j)))
