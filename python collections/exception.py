try:                                        
    b={3:'mango'}
    print(b[3])        
except ZeroDivisionError:
        print("Can't divide a number by zero")
except IndexError:
        print("Invalid Index")
except ValueError:
        print("Invalid Value")
#except KeyError:
#       print("Invalid Key")
except AttributeError:
        print("Invalid Attribute")
except NameError:
        print("Invalid Name")
except TypeError:
        print("Invalid Data Type")
except BaseException :
    print("Please give valid variables or values")
else:
    print("Thanks for choosing mango")
finally:
    print("program over")

try:
    a=30
    b=40
    c=a+b
    if c>100:
        raise Exception("sum exceeds 100")
    print(d)
except ValueError:
    print("Has some error")
