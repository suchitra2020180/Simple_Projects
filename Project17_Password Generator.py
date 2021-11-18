###Project17:  Password Generator

## How many letters you need in your password
# How many Symbols
#  How many Numbers
## Generate random values in req number for letters,numbers and symbols
## Add them

import string
import random
#len_password=input("What should be the length of your password? ")
num_of_lower_case_letters=int(input("How many lower case letters you need in your password: "))
num_of_upper_case_letters=int(input("How many upper case letters you need in your password: "))
num_of_symbols=int(input("How many symbols you need in your password: "))
num_of_numbers=int(input("How many numbers you need in your password: "))

lower_case_letters=[letter for letter in string.ascii_lowercase]
symbols=['!', '@', '#', '$', '%', '&','*', '(',')']
numbers= ['0','1','2','3','4','5','6','7','8','9']
upper_case_letters=[lower_case_letters[i].upper() for i in range(0, len(lower_case_letters))]
#print(lower_case_letters)
#print(symbols)
#print(numbers)
#print(upper_case_letters)

### Select characters for the password
#lower_case=random.choice(lower_case_letters)
req_lower_case=[]
for i in range(0, num_of_lower_case_letters):
    random_select=random.choice(lower_case_letters)
    #req_lower_case = req_lower_case + random_select
    req_lower_case.append(random_select)

print("Random lower case:",req_lower_case)

req_upper_case=[]
for i in range(0, num_of_upper_case_letters):
    req_upper_case.append(random.choice(upper_case_letters))

req_symbols=[]
for i in range(0, num_of_symbols):
    req_symbols.append(random.choice(symbols))

req_numbers=[]
for i in range(0, num_of_numbers):
    req_numbers.append(random.choice(numbers))


print("Random Upper case:",req_upper_case)
print("Random Symbols:",req_symbols)
print("Random Numbers:",req_numbers)

my_password_list=req_lower_case + req_upper_case + req_symbols + req_numbers
print("My password list:", my_password_list)

easy_password=""
for i in range(0, len(my_password_list)):
    easy_password += my_password_list[i]
print("====> Easy Password with pattern:", easy_password)

##Creating hard password

#my_password_list=random.shuffle(my_password_list)  ##is a problem
random.shuffle(my_password_list) 
print("Shuffled Password list:", my_password_list)
hard_password=""
for i in range(0,len(my_password_list)):
    hard_password += my_password_list[i]

print("===> Hard Password with no pattern:", hard_password)
