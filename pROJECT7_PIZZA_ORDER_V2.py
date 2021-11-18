print("Welcome to pizza delivery python code")

size=input("Which size of pizza do you want- S for small, M for medium, L for large: ")
add_pepperion=input("Do you want peperion - Y for Yes ,N for No: ")
extra_cheese=input("Do you want extra cheese- Y for Yes, N for No:")

bill=0

if size=='S':
    bill +=15
elif size=='M':
    bill +=20
else:
    bill +=25

if extra_cheese=='Y':
    bill +=1

if add_pepperion=='Y':
    if size=='S':
        bill +=2
    else:
        bill +=3

print(f"Your total bill is {bill}")