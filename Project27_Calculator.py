# Project 27:  Calculator

from ascii_logos import cal_logo #problem here

def add(n1,n2):
    result=n1+n2
    return result

def subtract(n1,n2):
    result=n1-n2
    return result

def multiply(n1,n2):
    result=n1*n2
    return result

def divide(n1,n2):
    result=n1/n2
    return result


def calculator():
    print(cal_logo)

    first_num=float(input("Enter the first number: "))
    #operator= input("Enter the operator 'sum for +', 'subtract for -', 'multiply for *','divide for /'")
    continue_operation="yes"
    while continue_operation=="yes":
        operators={
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide}
        for symbol in operators:
            print (symbol)
        operator= input("Enter the operator: ")
        sec_num=float(input("Enter another number: "))

        if operator=="+":
            result=add(first_num,sec_num)
        elif operator=="-":
            result=subtract(first_num,sec_num)
        elif operator=="*":
            result=multiply(first_num,sec_num)
        elif operator=="/":
            result=divide(first_num,sec_num)


        print(f"{first_num} {operator} {sec_num} = {result}")
        sec_num=0
        first_num=result
        user_input=str.lower(input("Want to continue operations- type 'y' for yes and 'N' for no :"))
        if user_input=='y':
            continue_operation="yes"
        else:
            continue_operation="No"
            calculator()


calculator()


