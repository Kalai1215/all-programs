'''class music:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c=self.a+self.b
        
    #print(c)
    def songs(self):
        print("fav singers",self.c)
obj=music('U1','Sid1')
#print(obj.c)
#print(obj.b)
obj.songs()

print("-----------------------------------------------")

class bread:
    def fun1(self,a,b):
        self.a=a
        self.b=b
    def fun2(self):
        print(self.a,"is same as",self.b)
obj=bread()
obj.fun1("kalai","arasi")
obj.fun2()

print("-----------------------------------------------")

class div:
    a=2
    b=3
    print(a+b)
    
print("-----------------------------------------------")

class green:
    def s(self):
        a="kalai"
        b="arasi"
        print(a+b)
obj=green()
obj.s()

print("-----------------------------------------------")

class green:
    def __init__(self,num):
        print("The number decalred in constructor is",num)
obj=green(12)


print("-----------------------------------------------")

class blue:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def sub(self):
        print(self.name,"\'s lucky number is",self.num)
obj=blue("kalai",12)
obj.sub()

print("-----------------------------------------------")

class blue:
    def colour(self,name,num):
        self.name=name
        self.num=num
    def sub(self):
        print(self.name,"\'s lucky number is",self.num)
obj=blue()
obj.colour("kalai",12)
obj.sub()

print("-----------------------------------------------")

class andrea:
    def __init__(self):
        print("Constructor")
    def __del__():
        print("Destructor")
obj=andrea()

print("-----------------------------------------------")

print("even numbers:",list(i for i in range(0,101,2)))
print("odd numbers:",list(i for i in range(1,101,2)))

print("-----------------------------------------------")
#appdividend
class employee:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("The name of employee is:",self.name)
first=employee("Rushabh")
second=employee("Dhaval")
second.display()
first.display()

print("-----------------------------------------------")'''
#software testing help
'''class addition:
    a=10
    b=20
    def add(self):
        sum=addition.a+addition.b
        print("Sum of a and b is:",sum)
        
    def sub(self):
        sub=addition.a-addition.b
        print('sub of a and b is:',sub)
        super().sub()
        
class subraction:
    c=50
    d=10
    def sub(self):
        minus=self.c-self.d
        print("Subraction of c and d is:",minus)
class multiplication(addition,subraction):
    def mul(self):
        final=self.a*self.c
        print("Multiplication of a and c is:",final)
        super().sub()
ob=multiplication()
ob.mul()
ob.add()
ob.sub()'''


print("-------------------------------------------------")
#pythoninsta planet
'''class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
john=student("John",98)
bob=student("Bob",89)
print(john.name)
print(john.grade)
print(bob.name)
print(bob.grade)

print("-------------------------------------------------")
#simplilearn
class person:
    def __init__(self,name,age=0):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
mem=person("Sam",20)
mem.display()
print(mem.name)
print(mem.age)
print(mem.name,"is",mem.age,"years old")

print("-------------------------------------------------")

#towards data science
class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def __repr__(self):
        return "My car is {} and was produced by {}".format(self.color,self.brand)
obj=car("Tesla","Fluorescent")
print(obj)
print(obj.brand)
print(obj.color)

print("-------------------------------------------------")

#python.org
class dog:                    
    tricks=[]
    def __init__(self,name):
        self.name=name
        print(self.name)
    def add(self,trick):
        self.tricks.append(trick)
d=dog("Fido")
e=dog("Buddy")
d.add("roll over")
e.add("play dead")
print(d.tricks)

print("-----------------------------------------------")
#Methods
#Methods are functions defined inside the body of a class.
#They are used to define the behaviors of an object.
#Example 2 : Creating Methods in Python
#programiz
class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("Happy"))
print(blu.dance())

print("----------------------------------------------------")

#Inheritance
#Inheritance is a way of creating a new class for using details of an
#existing class without modifying it.
#The newly formed class is a derived class (or child class).
#Similarly, the existing class is a base class (or parent class).
#Example 3: Use of Inheritance in Python

#parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()

print("-----------------------------------------------------")

#Encapsulation
#Using OOP in Python, we can restrict access to methods and variables.
#This prevents data from direct modification which is called encapsulation.
#In Python, we denote private attributes using underscore as the prefix
#i.e single _ or double __.
#Example 4: Data Encapsulation in Python

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

print("------------------------------------------------------")

#Polymorphism
#Polymorphism is an ability (in OOP) to use a common interface
#for multiple forms (data types).
#Suppose, we need to color a shape, there are multiple shape options
#(rectangle, square, circle). However we could use the same method
#to color any shape. This concept is called Polymorphism.
#Example 5: Using Polymorphism in Python

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)





class num:
    def __init__(self):
        print("hello")
    def new(self):               #(self,a,b)
        self.a="kalai"           #self.a=a
        self.b="arasi"           #self.b=b
        print("Her full name is",self.a+self.b)
class num2(num):
    def __init__(self):
        print("hi")
       # super().__init__()
        self.c="nail"
        self.d="polish"
    def new2(self):
        print("She has",self.c+self.d)
obj=num2()
obj.new()                       #("kalai","arasi")
obj.new2()


class key:
    def __init__(self):
        print("Constructor of A")
    def rose(self):
        a=input("Enter something")        
class keyword:
    def __init__(self):
        print("Constructor of B")
    def new(self):
        print("class keyword")
        
class word(key,keyword):
    def __init__(self):
        print("Constructor of C")
    def rose(self):
        print("class word")
    def super(self):
        super().__init__()
#obj=key()
#key.rose()
obj=word()
obj.super()
obj.new()
obj.rose()

print("--------------------------------------------------------")

class ice:
    def cream(self,name,flavour):
        print(name,"\'s fav ice cream flavour is",flavour)
class melt(ice):
    def __init__(self):
        self.fname='kalai'
        self.lname="arasi"
        print(self.fname+self.lname)
obj=melt()
obj.cream("kalai","chocolate")
    
print("--------------------------------------------------------")

class MyClass:
    x=5
    print(x)
MyClass

print("-----------------------------------------------------------------")

class numbers:
    def __init__(self):
        x=int(input("Enter a number:"))
        y=int(input("Enter a number:"))
        self.x=x
        self.y=y
    def sum(self):
        b=self.x+self.y
        print("The sum is:",b)
    def sub(self):
        b=self.x-self.y
        print("The sub is:",b)
    def mul(self):
        b=self.x*self.y
        print("The multiplied value is:",b)
    def div(self):
        b=self.x/self.y
        print("The divided value is:",b)
obj=numbers()
obj.sum()
obj.sub()
obj.mul()
obj.div()

print("-----------------------------------------------------------------")

class method:
    def __init__(self):
        self.a=5
        self.b=5
    
    def mod(self):
        print(self.a+self.b)
obj=method()
obj.mod()

print("-----------------------------------------------------------------")

class add:
    def add(self):
        print("Addition:",self.a+self.b)
class sub(add):
    def sub(self):
        print("Subraction:",self.a-self.b)
class mul(sub):
    def mul(self):
        print("Multipication:",self.a*self.b)
class div(mul):
    def div(self):
        print("Division:",self.a/self.b)
class final(div):
    def __init__(self,a,b):
        self.a=a
        self.b=b
obj=final(5,5)
obj.add()
obj.sub()
obj.mul()
obj.div()


class bala:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(name)
        print(self.name)
        print(age)
        print(self.age)
        
    def bala2(self):
        print(self.name,"age is",self.age)
obj=bala("love",43)
obj.bala2()
obj2=bala("affection",34)
obj2.bala2()
print("--------------------------------------------------------")

class Square:

    @staticmethod
    def get_squares(a, b):
        return a*a, b*b

print(Square.get_squares(3, 5))

print("--------------------------------------------------------")
#Every Python object has a __str__ method by default.
#When you use the object as a string, the __str__ method is called,
#which by default prints the memory location of the object.
#However, you can provide your own definition for the __str__ method as well.

class Car:
    def __str__(self):
        return "Car class Object"

    def start(self):
        print ("Engine started")

car_a = Car()
print(car_a)

print("-------------------------------------------------------")

class Car:

    # create class attributes
    car_count = 0

    # create class methods
    def __init__(self):
        Car.car_count +=1
        print(Car.car_count)
car_a = Car()
car_b = Car()
car_c = Car()

print('---------------------------------------------------------')

class Car:
    def start(self):
        message = "Engine started"
        return message
car_a = Car()
#print(car_a.message)

print("-------------------------------------------------------")

class Car:
    message1 = "Engine started"

    def start(self):
        message2 = "Car started"
        return message2

car_a = Car()
print(car_a.message1)
#print(car_a.message2)
print("---------------------------------------------------------")
class Car:
    def __init__(self):
        print ("Engine started")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 1999
obj=Car()
#get name
#get __make

print('--------------------------------------------------------')
class Car:

    # Creates Car class constructor
    def __init__(self, model):
        # initialize instance variables
        self.model = model

    # Creates model property
    @property
    def model(self):
        return self.__model

    # Create property setter
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return "The car model is " + str(self.model)
    
carA = Car(2088)
print(carA.getCarModel())
car_a = Car(2088)
#print(car_a.get_car_model())

print("--------------------------------------------------------")

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
#obj
#call
def kalai(bb,food,cycle):
    print(f'to play:{bb}\ninterest to eat:{food}\nmy transpotation usage is:{cycle}')
kalai('batminton','spiece item','shoes')

def varshu(id,name):
    return('student : {}\nstudent name : {}'.format(id,name))
    print

print("--------------------------------------------------------")

class Student:
    student_name='Malavika'
    dob='29/07/18'
obj=Student()
print('Student=',obj.student_name)
print('dob=',obj.dob)

obj.student_name='Nithyashree'
obj.dob='31/01/83'
#Student.student_name='Nithyashree'
#Student.dob='31/01/83'
print('Student=',obj.student_name)
print('dob=',obj.dob)


obj2=Student()
print('Student2=',obj2.student_name)
print('dob2=',obj2.dob)

print('-----------------------------------------------------')

class Student:
    school = 'Forward Thinking'
    address = '2626/Z Overlook Drive, COLUMBUS' 
student1 = Student()
student2 = Student() 
student1.student_id = "V12"
student1.student_name = "Ernesto Mendez"
student2.student_id = "V12"
student2.marks_language = 85
student2.marks_science = 93
student2.marks_math = 95 
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')

print('-----------------------------------------------------')

d=((1,'f'),(2,'b'),(3,'a'),(4,'r'))
x=sorted(d,key=lambda x:x[1])
print(x)

d=[(1,'f'),(2,'b'),(3,'a'),(4,'r')]
d.sort(key=lambda x:x[1])
print(d)

print('----------------------------------------------------')

a=[10,3,60,20,7]
target=80
for i in a:
    for j in a:
        if i+j==target:
            print((i,j))

print('---------------------------------------------------')

a=[10,2,4,7,-13,-4,-7]

for i in a:
    for j in a:
        if i+j==0:
            print([i,j])
        else:
            for k in a:
                if i+j+k==0:
                    print([i,j,k])

print('--------------------------------------------------')

for i in range(1,11):
    for j in range(1,11):
        print(i,'**',j,'=',i**j)

print('--------------------------------------------------')

a=(3,4,2,'bala','raj','amala')
v=[]
w=[]
for i in a:
    if int(i)==i:
        v.append(i)
    else:
        w.append(i)
print(v)
print(w)

print('--------------------------------------------------')

number = int(input("Enter a positive integer: "))
rev = 0
while(number!=0):
    digit = number%10
    rev = (rev*10)+digit
    number = number//10
print(rev)

print('--------------------------------------------------')'''

'''def student(name,age):
    print(name)
    print(age)
student('kalai',23)

print('--------------------------------------------------')

def student_data(student_name=None,student_class=None,student_id=None):
    if student_id is not None:
        print('Student id:',student_id)
    if student_name is not None:
        print(student_name)
    if student_class is not None:
        print(student_class)

student_data(student_id='01',student_name='kalai',student_class='XII')

print('--------------------------------------------------')

class Student:
    pass
print(type(Student))
print(Student.__dict__.keys())
print(Student.__module__)

print('--------------------------------------------------')

class student:
    pass
class marks:
    pass
S=student()
M=marks()

print(isinstance(S,student))
print(isinstance(M,marks))
print(issubclass(student,object))
print(issubclass(marks,object))

print('--------------------------------------------------')

class student:
    student_name='kalai'
    marks=200
print(student.student_name)
print(student.marks)
student.student_name='ria'
student.marks=500
print(student.student_name)
print(student.marks)

print('--------------------------------------------------')

class student:
    id=10
    name='kalai'
student.class1='XII'
print(student.id)
print(student.class1)
print(student.name)
del student.name

print(student.id)
print(student.class1)
#print(student.name)

print('--------------------------------------------------')

class student:
    id=10
    name='name'
    def num():
        print(student.id)
        print(student.name)
student.num()

print('--------------------------------------------------')

class Student:
    pass 
student1 = Student()
student2 = Student() 
student1.student_id = "V12"
student1.student_name = "Ernesto Mendez"
student2.student_id = "V12"
student2.marks_language = 85
student2.marks_science = 93
student2.marks_math = 95 
students = [student1, student2]
for student in students:
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')

print('--------------------------------------------------')

class find:
    num= [10,20,10,40,50,60,70]
    target=50
    for i in num:
        for j in num:
            if i+j==target:
                print(index(i),index(j))'''



def g():
    s=[1,2,3,4,5,5]
for i in g():
    print(i)







                
                
