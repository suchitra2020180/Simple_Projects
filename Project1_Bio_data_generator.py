##Project1: Biodata generator
Name=input("Enter your full name:  ")
Gender=input("Enter your gender: ")
DOB=input("Enter your Date of Birth :")
Qualification=input("Enter your Qualification :")
lang=[]
Num_languages_known=int(input("Number of Languages known : "))
for i in range(0,Num_languages_known):
    languages=input("Enter the language known: ")
    lang.append(languages)

print("=========   Biodata  ============")
print("Name : ", Name)
print("Gender : ",Gender)
print("Date of Birth : ", DOB)
print("Qualification : ", Qualification)
print('Lnguages known: ',lang)


