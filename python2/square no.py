for i in range(0,10):
    print('the square of',i,'is',i*i)
    i+=1
    
fact=1
n=int(input('enter a number'))
for i in range(1,n+1):
    fact=fact*i
    i+=1
    print('the factorial of',n,'is:',fact)
