'''c={}
a='bala is a student and he is from chennai,he interest explore bike riding and variety of foods and sports'
for i in a:
    k=c.keys
    if i in k():
        c[i]+=1
        #print('2',c)
    else:
        c[i]=1
        #print('1',c)
print(c)
        
        

b='balasubramani'
print(b.count('a'))

print(a)

print(a.count('a'))

def bala(a):
    x=[]
    for i in a:
        x.append(i)
        #print(x.count(i))
    c=dict.fromkeys(a,a.count(x))
    print(c)
    
bala(bala is a student and he is from chennai)'''

'''v=('a','a','c','x','v')
x=(4)
c=dict.fromkeys(v,x)
print(c)

z='bala is a student and he is from chennai'
a=set()
sum=1
for i in z:
    n=dict.fromkeys(i,z.count(i))
    a.add(n)
print(a)

z='bala is a student and he is from chennai,he interest explore bike riding and verity if foods and sports'
h=[]
g=[]
for i in z:
    h.append(i)
    g.append(z.count(i))
#print(h)
#print(g)
n=dict.fromkeys(h,z.count(i))
print(n)'''

a='something'
print(len(a))

print('---------------------------------------------')

a='kalaiarasi'
num={}
for i in a:
    x=num.keys
    if i in x():
        num[i]+=1
    else:
        num[i]=1
print(num)

print('---------------------------------------------')

str='length'
if len(str)<2:
    print('')
else:
    print(str[:2]+str[-2:])

print('---------------------------------------------')
        
def char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = str1[1:]

  return char+str1
print(char('restart'))

a='thoughts'
z=a[0]
new=a.replace(z,'$')
print(z+new[1:])

a='thoughts'
z=a[1]
new=a.replace(z,'$')
print(new[0]+z+new[2:])

print('---------------------------------------------')

a,b='apple','banana'
x=a[:2]
y=b[:2]
print(a.replace(x,y),end=' ') #a.replace(a[:2],b[:2])
print(b.replace(y,x)) #b.replace(b[:2],a[:2])

print('---------------------------------------------')

a='raining'

if len(a)<3:
    print(a)
else:
    if a[-3:]=='ing':
        print(a+'ly')
    else:
        print(a+'ing')

print('---------------------------------------------')

a='The lyrics is not that poor'
b=a.find('not')
c=a.find('poor')
if c>b and b!=0 and c!=0:
    d=a.replace(a[b:c+4],'good')
    print(d)
else:
    print(a)

print('---------------------------------------------')

a=['apple','banana','strawberry','grape','mango']
b=[]
for i in a:
    b.append((len(i),i))
#print(b)
b.sort()
#print(b)
print('larwd:',b[-1][1])
print('len:',b[-1][0])

print('---------------------------------------------')

a='student of class 12'
n=int(input('n th value:'))
b=a.replace(a[n],'')
print(b)

print('---------------------------------------------')

a='king'
print(a[-1]+a[1:-1]+a[0])

print('---------------------------------------------')

a='something to be spelt'
for i in range(0,len(a)+1,2):
    print(a[i],end='',sep='')
print()
print('---------------------------------------------')

a='ab cd ef df gh ij ab cd ef'.split()
d={}
for i in a:
    k=d.keys
    if i in k():
        d[i]+=1
    else:
        d[i]=1
print(d)

print('---------------------------------------------')

a=input('enter:')
b=a.upper()
c=a.lower()
print(b)
print(c)

print('---------------------------------------------')

a=input('enter:').split(',')
b={}
for i in a:
    k=b.keys
    if i in k():
        pass
    else:
        print(i)
