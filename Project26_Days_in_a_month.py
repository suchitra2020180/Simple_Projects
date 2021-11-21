## Project26_Days in a month or a given Year.



def is_leap_year(year):
    if year%100==0:
        if year%400 ==0:
            #print(f"{year} is  a leap year")
            return True
        else:
            #print(f"{year} is not a leap year")
            return False
    else:
        if year%4==0:
            #print(f"{year} is a leap year")
            return True
        else:
            #print(f"{year} is not a leap year")
            return False

year=int(input("Enter a year: "))
month =int(input("Enter the month number: "))
if is_leap_year(year):
    feb=29
else:
    feb=28

days_in_month=[31, feb,31,30,31,30,31,31, 30,31,30,31]
days= days_in_month[month-1] ##As we enter months from 1 to 12, used (month-1)
print(f" Year {year},month {month} has {days} days")