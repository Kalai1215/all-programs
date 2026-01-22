k=1
for i in range(3):
    for j in range(0,k):
        print("*",end=" ")
    k+=2
    print()
print()


for i in range(5):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
print()

for i in range(5,0,-1):
    for j in range(0,i-1):
        print(end=" ")
    for j in range(0,6-i):
        print("*",end=" ")
    print()
print()

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
print()

for i in range(0,5):
    for j in range(0,4-i):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
