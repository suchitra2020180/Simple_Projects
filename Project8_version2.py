##Ptoject 8 version2
print("=== Welcome to love calculator ===")
person1=input("Enter your name: ")
person2=input("Enter another name with whom you want to see the love score: ")

combined_names=person1+person2
str_combined= str.lower(combined_names)

t=str_combined.count('t')
r=str_combined.count('r')
u=str_combined.count('u')
e=str_combined.count('e')
true=t+r+u+e

l=str_combined.count('l')
o=str_combined.count('o')
v=str_combined.count('v')
e=str_combined.count('e')
love=l+o+v+e

Love_score=str(true)+ str(love)

print(Love_score)

if (Love_score < 10 or Love_score > 90):
    print(f"Your score is {Love_score}, you go together like coke and mentos")
elif (Love_score > 40 and Love_score < 50):
    print(f"Your score is {Love_score}, you are alright together")
else:
    print(f"Your score is {Love_score}")