## Project11: Banker Roulette
##In London, particularly in areas with financially rich,when they went to restaurent to pay the bill they use coupon code.
#when they need to pay the bill, they put their business code in the bowl, the person whose business code is selected have to pay the bill.

import random
All_names=str(input("Enter everybody's name ,seperated by comma:  "))
print(All_names)
names_list=All_names.split(',')
print("Names list given:",names_list)
print("Length of names_list:",len(names_list))
rand_name=random.randint(0, len(names_list)-1)
print("Random number:",rand_name)
print(f"{names_list[rand_name]} is going to pay the bill for the meal today")
