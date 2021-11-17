##Project4: Tip Calculator
##In restuarent we will have a bill and we want to give a tip of either 105 or 125 or 15%
##The money will be shared by our team members or friends.So how much each of us have to pay.
# 
# In this project we will calculate the money paid by each of our friends including you.

##First enter the bill
##Then select the percentge of tip we want to give
## Number of persons need to pay the bill

Total_bill=input("Enter the total bill: ")
#tips_percent= [10,12,15]
select_tip= input("Select any tip percetage you wish to give 10 or 12 or 15 %: ")
bill_with_tip=float(Total_bill)+ (float(Total_bill)*(int(select_tip)/100))
Num_of_persons=input("Enter number of persons: ")
each_share= bill_with_tip/int(Num_of_persons)
print("Share of each persons: ",round(each_share,2))