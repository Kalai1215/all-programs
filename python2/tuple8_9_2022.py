'''b=[]
a=[(7,6),(9,8),(1,2),(3,4),(2,3)]
for i in a:
    c=list(i)
    b.append(c)
print(b)
print(type(a))

x=[]
b=[(7,6),(9,8),(1,2),(3,4),(2,3)]
for i in b:
    v=sum(i)
    x.append(v)
print(x)

v=[]
z=(1, 2, 3, 4)
x=(3, 5, 2, 1)
c=(2, 2, 3, 1)
for i in range(4):
    a=z[i]+x[i]+c[i]
    v.append(a)
d=tuple(v)
print(d)

def bala1(tuple):
    return(tuple,key=bala)
bala1([(7,6),(9,8),(1,2),(3,4),(2,3)])

def bala(n): return n[-1]

def bala1(tuple):
    return(tuple,key=bala)
bala1([(7,6),(9,8),(1,2),(3,4),(2,3)])

v='white'
c='blue'
k='black'

a=(('Red', 'white', 'blue'), ('green', 'Pink', 'Purple'),
 ('Orange', 'Yellow', 'Lime'))

if v in a[0]:
    print('1yes')
else:
    print('not in range')
if c in a[1]:
    print('2yes')
else:
    print('not in range')
if k in a[2]:
    print('3yes')
else:
    print(k,'not in range')

a=('1','2','3','4')
x=int(''.join(a))
print(type(x))
        
def bala1(a):
    b=int(''.join(map(str,a)))
    return b
print(bala1((1,2,3,4)))

a=(('1,2'),('3,4'),('2,3,4'))
print(int(a))'''






a=('1','2','3','4')
for i in a:
    print(i,end='')
    


