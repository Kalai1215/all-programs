
for n in range(1,51):
    for i in range(2,n):
        a=n%i
        if a==0:
            
            break
        
    else:
        print(n,"prime number")
'''
names=['John','Jane','Smith']
j=0
for name in names:
    j+=1
    print('The name number ',j,' in the list is ',name)

wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

sqlist=[]
for x in range(1,11):
         sqlist.append(x*x)

print(sqlist)



sqlist=[x*x for x in range(1,11)]
print(sqlist)


sqlist=[x*x for x in range(1,11) if x%2 != 0]
print(sqlist)


a=[]
for i in range(5):
    for j in range(4):
        i+=i
        a.append(i)
    print(a)
    a=[]'''
for b in range(2,101):   
    for i in range(2,b):
        if b%i==0:
            break

    else:
        print(str(b),'prime')
