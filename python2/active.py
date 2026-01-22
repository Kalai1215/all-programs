a={'boy':'active','girl':'inactive','trans':'active'}
for i,j in a.copy().items():
    if j=='inactive':
        del a[i]
        print(a)
    
a1={}
for i,j in a.items():
    if a=='active':
        a1[i]=j
    print(a)
        
