for i in range(1,6):
    for j in range(1,6):
        if i+j>=6:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print("-----------------------------------------------")
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print("*",end=" ")
        else:
            print(end=" ")
    print()
print("-----------------------------------------------")
for i in range(1,6):
    for j in range(1,6):
        if i+j<=6:
            print("*",end=" ")
        else:
            print(end=" ")
    print()
print("-----------------------------------------------")
for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print("-----------------------------------------------")
space=4
for i in range(0,5):
    for j in range(0,space):
        print(end=" ")
    space-=1
    for j in range(0,i+1):
        print("*",end=" ")
    print()
print("-----------------------------------------------")
space=0
for i in range(5,0,-1):
    for j in range(0,space):
        print(end=" ")
    space+=1
    for j in range(0,i):
        print("*",end=" ")
    print()
