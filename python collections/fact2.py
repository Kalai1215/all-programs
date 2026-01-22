factorial=1
num=int(input("Enter a number:"))
if num<0:
    print("Factorial doesn\'t exist")
elif num==0:
    print("Factorial is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
        print("The factorial of",num,"is:",factorial)

def factorial(i):
    if i==1:
        return 1
    else:
        return i*factorial(i-1)
i=int(input("Enter a number:"))
print("The factorial is",factorial(i))

    
