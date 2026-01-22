n=int(input("Enter no. of inputs:"))
b=[]
c=[]
d=[]
#e=[]
#f=[]
for i in range(1,n+1):
    a=int(input("Enter a number:"))
    b.append(a)
b.sort()
#print(b)
for i in b:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)
#print('even num:',c)
#print('odd num:',d)
d.reverse()

for x in range(3):
    print(c[x],end=" ")
    #e.append(c[x])
    
print('\n')

for y in range(3):
    print(d[y],end=" ")
    #f.append(d[y])
print('\n')
#print('3 largest odd num:',f)
#print('3 smallest even num:',e)
