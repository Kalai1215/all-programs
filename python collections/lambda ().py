x=lambda a:a+10 #15
print(x(5))
print("---------------------------------------------")
x=lambda a,b:a*b #30
print(x(5,6))
print("---------------------------------------------")
def myfunc(n): #22
    return lambda a:a*n
my_doubler=myfunc(2)
print(my_doubler(11))
print("---------------------------------------------")
tables=[lambda x=x:(x*10) for x in range(1,11)] #4
for i in tables:
    print(i())
print("---------------------------------------------")
a=[1,2,3] #[1,2,3]
d=list(map(lambda x:x,a))
print(d)
print("---------------------------------------------")
a=[1,2,3] #[3,6,9]
d=list(map(lambda x:(x*3),a))
print(d)
print("---------------------------------------------")
a=[1,2,3]                       #3
d=list(map(lambda x:(x*3),a))   #6
for i in d:                     #9
    print(i)
print("---------------------------------------------")
a=[1,2,3]
d=list(map(lambda x:(x*3),a))
for i in range(3):
    for i in d:
        print(i)
print("---------------------------------------------")
a=[1,2,3] #9
for i in map(lambda x:(x*3),a):
    print(i)
print("---------------------------------------------")
for i in map(lambda x:(x*3),[4,5,6]): 
    print(i)
print("---------------------------------------------")
s=list(a for a in range(0,101))
b=list(filter(lambda x:(x%2==0),s))
print(b)
print("---------------------------------------------")
a=[11,22,33] 
b=(10,20,30)
for i in map(lambda x,y:(x+y),a,b):
    print(i)
a=(7,8,9)
b=(9,6,8)
c=(9,7,6)
for i in zip(a,b,c):
    print(i)



