k=1
for i in range(5):
    for j in range(i+1):
        k-=1
        print(k,end='  ',sep='')
        k+=1
    print()
