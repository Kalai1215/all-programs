k=1
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print(k,end=" ")
            k+=1
        else:
            print(end=" ")
    print()

k=1
for i in range(1,6):
    for j in range(1,6):
        if i+j>=6:
            print(k,end=" ")
            k+=1
        else:
            print(end="  ")
    print()
    
for i in range(1,6):
    for j in range(i,0,-1):
            print(j,end=" ")
    print()


k=0
for i in range(1,6):
    k+=1
    for j in range(1,6):
        print(k,end=" ")
        k-=1
    print()
