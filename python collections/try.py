def num():
	a=5
	b=3
	c=a+b
	return c
print("The Sum is:",num())


   
x=10*3
y=10*2
print('The value of x is '+str(x)+' and y is '+str(y))
print(type(str(x)))
print(type(y))



x=10*3
y=10*2
print('The value of x is',x,'and y is',y)
print(type(x))
print(type(y))



a=[]
b=[]
for i in range(1,101):
        if i%2==0:
                a.append(i)
        else:
                b.append(i)
print("The even numbers are:",a)
print("The odd numbers are:",b)

