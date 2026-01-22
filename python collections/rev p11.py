k=1
for i in range(1,6):
    for j in range(1,6):
        if j==4 and i>-1:
            print(k,end=" ")
            k+=1
        elif j==3 and i>0:
            print(k,end=" ")
            k+=1
        else:
            print(end=" ")
    print()

