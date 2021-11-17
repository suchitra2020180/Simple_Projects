##PROJECT3: lIFE IN WEEKS
#Lets us say we are fortunate to live upto 90 years.
##entering the Age will give you no. of years, weeks, days left
Age=input("Enter your present age: ")
#1year=365 days
#1year=52 weeks
#1week=7 days
Left_years=90-int(Age)
Left_weeks=Left_years *52
Left_days=Left_years*365
Left_months=Left_years*12
print("Left years:", Left_years)
print("left months:", Left_months)
print("Left weeks:", Left_weeks)
print("Left days:", Left_days)
print("You will live for {} years,{} months,{} weeks,{} days.".format(Left_years,Left_months,Left_weeks,Left_days))