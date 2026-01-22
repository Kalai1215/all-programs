# No Return Without Arguments

def bday():
    name="Ram"
    DOB="3.04.63"
    print(name,"birthday is on:",DOB)
bday()

# No Return With Arguments

def mail(name,id):
    print(name,"mail id is:",id)
mail("Ria","abc@gmail.com")
    
# With Return Without Arguments

def bank():
    name="Abi"
    account_number=85836587658
    return name,account_number

one,two=bank()
print(one," personal account number is",two)

# With Return With Arguments

def trip(name,loc):
    return name,loc

name,loc=trip("Guys","Goa")
print(name,"our destination is ",loc)

def func(name,loc):
    print(name,"is in",loc)
func("Mr.X","Delhi")
    

