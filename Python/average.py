s1,s2,s3,s4,s5=(int(input("Enter your tamil mark:")),int(input("Enter your english mark:")),int(input("Enter your maths mark:")),int(input("Enter your science mark:")),int(input("Enter your social mark:")))
if(34<s1<101 and 34<s2<101 and 34<s3<101 and 34<s4<101 and 34<s5<101):
    print("PASS")
    total=s1+s2+s3+s4+s5
    avg=total/5
    print("TOTAL MARKS OF THE STUDENT IS:",total)
    print("THE AVERAGE MARKS OF THE STUDENT IS:",avg)
else:
    print("FAIL")


m1=int (input("Enter mark in first subject : "))
m2=int (input("Enter mark in second subject : "))
m3=int (input("Enter mark in third subject : "))
m4=int (input("Enter mark in fourth subject : "))
m5=int (input("Enter mark in fifth subject : "))
m6=int (input("Enter mark in sixth subject : "))
avg= (m1+m2+m3+m4+m5+m6)/6
if avg>=80:
    print ("Grade : A")
elif avg>=70 and avg<80:
    print ("Grade : B")
elif avg>=60 and avg<70:
    print ("Grade : C")
elif avg>=50 and avg<60:
    print ("Grade : D")
else:
    print ("Grade : E")
