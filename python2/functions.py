#without argument without return
def bala():
    a="kalai"
    b="45"
    print(a,"'s age is",b)
    c=a+b
    print(c)
bala()

#without argument with return
def bala():
    name="kalai"
    flavour="chocolate"
    return (name+" fav flavour is "+flavour)
print(bala())
    
#with argument with return
def bala(name,flavour):
    return name+" fav flavour is "+flavour
print(bala("kalai","chocolate"))

#with argument without return    
def bala(a,b):
    c=a+b
    print(c)
bala(4,5)
