#1. Make a Username Generator from first and last names.
import random
def username(firstname,lastname):
    username = []
    if firstname and lastname != 0:
        username = firstname + lastname
        username += str(random.randint(10,99))
        return username
    
fname = str(input("Enter your first name: "))
lname = str(input("Enter your last name: "))
print("First name : ",fname)
print("Last name : ",lname)
print("Your username is",username(fname,lname))


