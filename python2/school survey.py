class bala:
    pass
sub1=int(input('enter a tamil mark :'))
sub2=int(input('enter a english mark :'))
sub3=int(input('enter a math mark :'))
sub4=int(input('enter a economics mark :'))
sub5=int(input('enter a histry mark :'))

total=sub1+sub2+sub3+sub4+sub5
avg=total/5
print('total marks are :',total)

x='pass' if sub1>34 and sub2>34 and sub3>34 and sub4>34 and sub5>34 else 'fail'
print('you got a' ,x,' mark')
if x=='pass' :
    print('average marks are :%d'%(avg))
    if avg in range (90,101):
        print('A grade')
    elif avg in range(80,90):
        print('B grade')
    elif avg in range(70,80):
        print('c grade')
    elif avg in range(60,70):
        print('d grade')
    elif avg in range(50,60):
        print('e grade')
    else:
        print('no grade')
    
else:
    print('unfortunatly you are fail so no average ')
    
