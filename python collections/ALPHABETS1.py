#A
for i in range(5):
    for j in range(3):
        if(j==0 or j==2)or(i==0 or i==2):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#B
for i in range(5):
    for j in range(3):
        if j==0 or(i%2==0 and j==1)or(j==2 and i%2==1):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#C
for i in range(5):
    for j in range(3):
        if(j==0 and(i==1 or i==2 or i==3))or((i==0 or i==4)and(j==1 or j==2)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#D
for i in range(5):
    for j in range(4):
        if j==0 or(j==1 and (i==0 or i==4))or(j==2 and(i==1 or i==3))or(i==2 and j==2):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#E
for i in range(5):
    for j in range(3):
        if j==0 or (i==0 or i==2 or i==4):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#F
for i in range(5):
    for j in range(3):
        if j==0 or i==0 or i==2:
            print("*",end=" ")
        else:
            print(end="   ")
    print()
print()
#G
for i in range(5):
    for j in range(4):
        if j==0 or i==0 or i==4 or((i==2 or i==3)and(j==2 or j==3)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#H
for i in range(5):
    for j in range(3):
        if j==0 or j==2 or i==2:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#I
for i in range(5):
    for j in range(3):
        if j==1 or i==0 or i==4:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#J
for i in range(5):
    for j in range(3):
        if((j==1 and i!=4)or i==0) or(i==3 and j!=2):
           print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#K
for i in range(5):
    for j in range(4):
        if j==0 or (i==2 and j==1)or(j==2 and i%2==1)or(j==3 and(i==0 or i==4)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#L
for i in range(5):
    for j in range(3):
        if j==0 or i==4:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#M
for i in range(5):
    for j in range(5):
        if j==0 or j==4 or (i==1 and j!=2) or (i==2 and j==2):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#N
for i in range(5):
    for j in range(5):
        if (j==0 or j==4)or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#O
for i in range(5):
    for j in range(3):
        if j==0 or j==2 or i==0 or i==4:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#P
for i in range(5):
    for j in range(3):
        if j==0 or (j==1 and(i==0 or i==2))or(i==1 and j==2):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#Q
for i in range(6):
    for j in range(5):
        if(j==0 and i<5)or(j==3 and i<5)or(i==0 and j<4)or(i==4 and j<4)or(i==3 and j==2):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#R
for i in range(5):
    for j in range(3):
        if j==0 or(j==1 and(i==0 or i==2))or(j==2 and(i==1 or i>2)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#S
for i in range(5):
    for j in range(3):
        if i==0 or i==2 or i==4 or(i==1 and j==0)or(i==3 and j==2):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#T
for i in range(5):
    for j in range(5):
        if j==2 or i==0:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#U
for i in range(5):
    for j in range(4):
        if (j==0 and i<4)or(j==3 and i<4)or(i==4 and(j==1 or j==2)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#V
for i in range(5):
    for j in range(9):
        if i==j or(i==3 and j==5)or(i==2 and j==6)or (i==1 and j==7)or(i==0 and j==8):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
print()
#W
for i in range(5):
    for j in range(5):
        if j==0 or j==4 or(i==2 and j==2)or(i==3 and j!=2):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#X
for i in range(5):
    for j in range(5):
        if j==i or(i==4 and j==0)or(i==3 and j==1)or(i==1 and j==3)or(i==0 and j==4):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#Y
for i in range(5):
    for j in range(5):
        if (i==0 and(j==0 or j==4))or(i==1 and j%2==1)or(j==2 and i>1):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print()
#Z
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or(i==3 and j==1)or(i==2 and j==2)or(i==1 and j==3):
            print("*",end=" ")
        else:
            print(end="  ")
    print()






