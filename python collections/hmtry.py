def val(mail,psd):
    return mail+psd
print("the mail and pass is:",val('abc','123'))

def val():                                      #2 arguments can't be
    mail='abc'                                  # printed while using 
    psd='123'                                   # return
    return mail+psd
print("the mail and pass is:",val())
def val():
    mail='abc'
    psd=123
    print("the mail is",mail,"and pass is",psd)
val()

def val(mail,psd):
    print("the mail is",mail,"and pass is",psd)
val('abc',123)
    
#arbitary ()
def hab(*var):
    print(var)
hab('a','b','c','d')

def hab(nm,*db):
    print('hello',nm)
    #print('things:',db)
    for i in db:
        print(i)
hab('sid','a','b','c','d')

def pwd(**name):
    for i,j in name.items():
        print("%s:%s"%(i,j))
pwd(name='sid',age='23',dob='1.2.3')

# recursive function
def jai(n):
    if n==0:
        return 0
    else:
        print(n)
        return jai(n-1)
print(jai(10))                    #jai(10) o/p: upto 1 (0 wont be there)

def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(argument, "Invalid month"))

x={i : i+2 for i in range(5)}
print(x)
for i in range(0,20):
    if i==6:
        continue
    print(i)

        
def num():
    a='IAM BALA from karur'
    for i in a:
        if i.isupper()==True:
            print(i)
num()

def ab(*lists):
    a=list(lists)
    a.reverse()
    print(a)
ab(1,2,3,4,'a','b')

def num(a):
    sum=0
    for i in a:
        #print(i)
        sum+=1
    #print(sum)
    for j in range(-1,-sum-1,-1):
        #print(i)
        print(a[j],end='')
num('123abc')

a=input('Enter your name:')
print(a*2)

'''N=int(input())
X=int(input())
A=[]
for i in range(N):
    A.append(int(input()))
count=0
for i in range(N):
    temp=0
    for j in range(i,N):
        temp=temp^A[j]
        if (temp<X):
            count+=1
print(count)'''

def new(z):
    return z[-1]
def num(tuples):
    return sorted(tuples,key=new)
a=[(1,3),(3,2),(2,1)]
print(num(a))

def ST(tup):
    List=len(tup)
    for i in range(0,List):
        for j in range(0,List-i-1):
            if(tup[j][-1]>tup[j+1][-1]):
                temp=tup[j]
                tup[j]=tup[j+1]
                tup[j+1]=temp
    return tup
tup=[(1,3),(3,2),(2,1)]
print(ST(tup))

def st(tup):
    tup.sort(key=lambda x:x [-1])
    return tup
tup=[(1,3),(3,2),(2,1)]
print(st(tup))


def add(a):
    if len(a)==1:
        return a[0]
    else:
        return a[0]+add(a[1:])
print(add([1,2,3,4]))


a=['e-wall is a private e-wall that is one of a private']
n=a[0].split()
c=set()
for i in n:
    c.add(i)
for i in c:
    n.remove(i)
for i in n:
    print(i)

a=[]
a1=[]
b=[]
b2=[]
c=[]
c2=[]
for i in range(1,1001):
    if len(str(i))==1:
        if i%2==0:
            a.append(i)
        else:
            a1.append(i)
    elif len(str(i))==2:
        if i%2==0:
            b.append(i)
        else:
            b2.append(i)
    else:#elif 
        if i%2==0:
            c.append(i)
        else:
            c2.append(i)
print(a)
print(a1)
print(b)
print(b2)
print(c)
print(c2)

s=4
for i in range(1,6):
    k=1
    n=k
    m=k
    for j in range(s):
        print(end=' ')
    s-=1
    for j in range(i):
        print(k,end=' ')
        if i>=3:
            if k==n or k==n+k:
                k=m+n
            else:
                k=n
    print()   
        

