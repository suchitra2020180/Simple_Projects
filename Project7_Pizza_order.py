print("Welcome to pizza delivery python code")

size=input("Which size of pizza do you want- S for small, M for medium, L for large: ")
add_pepperion=input("Do you want peperion - Y for Yes ,N for No: ")
extra_cheese=input("Do you want extra cheese- Y for Yes, N for No:")
small_size_pepperion_cost=2
med_or_large_size_pepperion=3
#extra_cheese_cost=1
small_size_pizza=15
med_size_pizza=20
large_size_pizza=25


if extra_cheese=='Y':
    extra_cheese_cost=1
else:
    extra_cheese_cost=0


if add_pepperion== 'Y':
    if size=='S':
        pep_cost=small_size_pepperion_cost
    else: 
        pep_cost=med_or_large_size_pepperion
else:
    pep_cost=0

if (size=='S' and extra_cheese=='Y'and add_pepperion=='Y'):
    print("Cost :",(small_size_pizza + pep_cost + extra_cheese_cost))
elif (size=='S' and extra_cheese=='Y'and add_pepperion=='N'):
    print("Cost :",(small_size_pizza + pep_cost + extra_cheese_cost))
elif (size=='S' and extra_cheese=='N'and add_pepperion=='Y'):
    print("Cost :",(small_size_pizza + pep_cost + extra_cheese_cost))
elif (size=='S' and extra_cheese=='N'and add_pepperion=='N'):
    print("Cost :",(small_size_pizza + pep_cost + extra_cheese_cost))   
elif (size=='M' and extra_cheese=='Y'and add_pepperion=='Y'):
    print("Cost :",(med_size_pizza + pep_cost + extra_cheese_cost))  
elif (size=='M' and extra_cheese=='N'and add_pepperion=='Y'):
    print("Cost :",(med_size_pizza + pep_cost + extra_cheese_cost)) 
elif (size=='M' and extra_cheese=='Y'and add_pepperion=='N'):
    print("Cost :",(med_size_pizza + pep_cost + extra_cheese_cost)) 
elif (size=='M' and extra_cheese=='N'and add_pepperion=='N'):
    print("Cost :",(med_size_pizza + pep_cost + extra_cheese_cost)) 
elif (size=='L' and extra_cheese=='Y'and add_pepperion=='Y'):
    print("Cost :",(large_size_pizza + pep_cost + extra_cheese_cost)) 
elif (size=='L' and extra_cheese=='N'and add_pepperion=='Y'):
    print("Cost :",(large_size_pizza + pep_cost + extra_cheese_cost))
elif (size=='L' and extra_cheese=='Y'and add_pepperion=='N'):
    print("Cost :",(large_size_pizza + pep_cost + extra_cheese_cost))   
else:
    print("Cost :",(large_size_pizza + pep_cost + extra_cheese_cost))




