
for i in range(5):
    for j in range(i,5):
        print("*",end=" ")
    print()
    
for i in range(5):
    for j in range(5):
        if i<=j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()

for i in range(5):            
    for j in range(i+1):
        print("*",end=" ")
    print()
    
for i in range(5):
    for j in range(5):
        if i+j>=4:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
    
import random
a=[i for i in range(1,10)]
print(random.choice(a))
    
import random
a=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(a))
