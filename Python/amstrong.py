num=int(input("Enter a 3 digit number:"))
a=int(str(num)[0])**3
b=int(str(num)[1])**3
c=int(str(num)[2])**3

if a+b+c==num:
    print(num,"is an amstrong number")
else:
    print(num,"is not an amstrong number")


