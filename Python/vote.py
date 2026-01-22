'''def vote():
    name=input("Enter your name: ")
    print(name,"please enter your age: ",end="")
    age=int(input(""))

    if age>=18:
        x="You are eligible to vote."
        print(x)
    else:
        x="You are not eligible to vote."
        print(x)
        return name,age
for i in vote():
    print(name,"age is",age,x)
    print(i)'''
    

name=input("Enter your name: ")
print(name,"please enter your age: ",end="")
age=int(input(""))

if age>=18:
    print("You are eligible to vote.")
        
else:
    print("You are not eligible to vote.")
        
        


