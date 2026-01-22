def pattern():
    num=int(input("Enter a number:"))
    space=num-1
    for i in range(0,num):
        for j in range(space):
            print(end=" ")
        space-=1
        for j in range(0,i+1):
            print("*",end=" ")
        print()
    space=0
    for i in range(num,0,-1):
        for j in range(space):
            print(end=" ")
        space+=1
        for j in range(0,i):
            print("*",end=" ")
        print()
