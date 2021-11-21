###Project25:Function with arguements
##Enter first and last name in lowercase or uppercase. We will change /format your name to Title case
import string

def format_name(fname,lname):
    name=fname + ' ' +lname
    formatted=name.title()
    print(formatted)



first_name=input("Enter First name: ")
last_name=input("Enter last name: ")
format_name(first_name, last_name)
