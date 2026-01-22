num=int(input("Enter the number:"))
fact=1
i=1
while num>=i:
    fact=fact*i
    i+=1
print("The factorial of",num,"is:",fact)


num=7
fact=1
for i in range(1,num+1):
    fact=fact*i
print('factorial of',num,'is',end='')
print(fact)


import math
print('factorial of 5 is',end='')
print(math.factorial(5))


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

