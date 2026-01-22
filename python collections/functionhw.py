def mod1():
    num=int(input("Enter a number:"))
    space=num-1
    for i in range(0,num):
        for j in range(space):                      # Enter a number: 5
            print(end=" ")                          #        *
        space-=1                                    #       * *
        for j in range(0,i+1):                      #      * * *
            print("*",end=" ")                      #     * * * *
        print()                                     #    * * * * *
    space=0                                         #    * * * * *
    for i in range(num,0,-1):                       #     * * * *
        for j in range(space):                      #      * * *
            print(end=" ")                          #       * *
        space+=1                                    #        *
        for j in range(0,i):
            print("*",end=" ")
        print()

mod1()

def mod2():
    age=int(input('Enter your age:'))
    m1,m2,m3,m4,m5=(int(input('Enter your eng mark:')),int(input('Enter your tamil mark:')),int(input('Enter your maths mark:')),int(input('Enter your science mark:')),int(input('Enter your social mark:')))
    total=m1+m2+m3+m4+m5
    avg=total/5
    print("Average:",avg)
    if avg>90:
        print("Grade A")
    elif avg>80 and avg<90:
        print("Grade B")
    elif avg>70 and avg<80:
        print("Grade C")
    else:
        print("Grade E")
mod2()

def mod3():
    a=int(input('Enter a number:'))
    b=int(input('Enter a number:'))
    print("Addition:",a+b)                      #Enter a number:5  
    print("Subraction:",a-b)                    #Enter a number:6
    print("Multiplication:",a*b)                #Addition:11
    print("Division:",a/b)                      #Subraction:-1
mod3()                                          #Multiplication:30
                                                #Division:0.0
                                                
    
