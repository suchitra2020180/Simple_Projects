##Project2 : Bio Mass Index Calculator (BMI)
weight= int(input ("Enter your weight in kg: "))
height=float(input("Enter your height in m: "))
BMI= float(round(weight/(height**2)))
# print("Your BMI is {} kg/m2".format(BMI))
print(BMI)
if BMI < 18.5:
    print("Your BMI is {} kg/m2 and you are underweight".format(BMI))
elif (BMI > 18.5 and BMI < 25):
    print("Your BMI is {} kg/m2 and you are Normal weight".format(BMI))
elif (BMI > 25 and BMI < 30):
    print("Your BMI is {} kg/m2 and you are slightly over weight".format(BMI))
elif (BMI > 30 and BMI < 35):
    print("Your BMI is {} kg/m2 and you are obese".format(BMI))
elif (BMI > 35):
    print("Your BMI is {} kg/m2 and you are clinically obese".format(BMI))
  