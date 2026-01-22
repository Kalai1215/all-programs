'''a='kalai#developer of india'
s=0
for i in a:
    s+=1
for j in range(-1,-s-1,-1):
    print(a[j],end='')
a=[]
b=[]
for i in range(1,10):
    if i%2==0:
       a.append(i)
    else:
        b.append(i)
        
print(a)
print(len(a))
print(b)
print(len(b))

a=[1452, 11.23, 1+2j, True,
 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
print(type(1452))
for i in a:
    print(i)
    print(type(i))
print(type(a))
print(list(a))
for i in range(0,7):
   
    if i==6 or i==3:
        continue

    print(i,end='')

a,b=0,1
while a<50:
    a,b=b,a+b
    if a<=50:
        print(a)


for i in range (1,51):
    if i%5==0 and i%3==0:
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('bizz')
    
    else:
        print(i)


j=0
k=0
l=0
m=0
b=[]
for i in range(4):
    #print([j,k,l,m],end=',')
    b.append([j,k,l,m])
    j+=0
    k+=1
    l+=2
    m+=3
    
print(b,end='')

rows= int(input("Input number of rows: "))
cols= int(input("Input number of columns: "))
multi_list = [[0 for col in range(cols)] for row in range(rows)]

for row in range(rows):
    for col in range(cols):
        multi_list[row][col]= row*col

print(multi_list)

a=input()
print(a.lower())
s=0
n=0
a='kalai17'
for i in a:
    #print(i)
    if i.isalpha():
        s+=1
    if i.isdigit():
        n+=1
        
print('letter',s)
print('numbers :',n)

x=['!','@','#','$','%','^','&','*']

z=input('create a password :')
for i in z:
    

    if  i in x:
        pass
    else:
        print('please use any spz character')
    if i.islower():
        pass
    else:
        print('plz use lower case also')
        
    if i.isupper():
        pass
    else:
        print('plz use upper case also')
    if i.isdigit():
        pass
    else:
        print('plz use digits')
            

    if len(z)<16 and len(z)>6:
        pass
    else:
        print('plz use min 6chr and maz 16 character')


import re
print(re.list())'''

for i in range(0,7):
    for j in range(0,5):
        if j==0 or (j<4 and i==0)or j==0 or (j==4 and 0<i<6) or (i==0 and 0<j<4)  or (i==6 and j<4):
            print('$',end=' ')
        else:
            print(end='  ')
    print('\n')

b=['a','e','i','o','u']
n=input()
if n in b:
    print(n,'is a vowel')
else:
    print(n,'is a consonant')

while True:
    a=['jan','mar','may','jul','sep','nov']
    n=input()
    if n in a:
        print('total days is : 31')
    elif n=='february':
        print('total days is:29/28')
        
        
    else:
        print('total days is :30')

a=int(input())
b=int(input())
c=a+b
if c is 15<c<20:
    print('sum of two is : 20')
else:
    print('sum of two is :',c)
        
            
    











    
           







