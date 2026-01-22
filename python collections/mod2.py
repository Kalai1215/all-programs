def average():
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
