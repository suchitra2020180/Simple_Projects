# Types of coffee and required ingredients
# Coffee machine requirements
# Coin operated==we have american coins penny: 1cent ($0.01), Nickel:5 cent ($0.05),
# Dime:10cent ($0.10) and Quarter:25cents ($0.25)
# Program requirements: a)create report of how much of the requirements such as coffee, water, milk are left
# b) Check if the resources are sufficient if the user orders a drink==> then order a drink
# c) Ask the user to insert a coin: Ask the user how many of particular type coins the user is using in machine
# d) give the user the left money
# e) if resources are no sufficient print no sufficient resources
# f)if money is sufficient then refund the money.Print sorry thats not
coffee = {
    "Espresso": {"Water in ml": 50,
                 "Coffee in grams": 18,
                 "Milk in ml": 0,
                 "Cost": 1.50},
    "Latte": {"Water in ml": 200,
              "Coffee in grams": 24,
              "Milk in ml": 150,
              "Cost": 2.50},
    "Cappuccino": {"Water in ml": 250,
                   "Coffee in grams": 24,
                   "Milk in ml": 100,
                   "Cost": 3.00}

}
print(coffee['Latte']['Cost'])

machine_resources = {"Water in ml": 300,
                     "Coffee in grams": 100,
                     "Milk in ml": 200,
                     "Cost": 0}

coins = {"Penny": 1,
         "Nickel": 5,
         "Dime": 10,
         "Quarter": 25}


def resource_sufficient(coffee_type):
    if machine_resources["Water in ml"] > coffee[coffee_type]["Water in ml"]:
        if machine_resources["Milk in ml"] > coffee[coffee_type]["Milk in ml"]:
            if machine_resources["Coffee in grams"] > coffee[coffee_type]["Coffee in grams"]:
                resource_status = 'OK'
                # print(f"Here is your {user_input}. Enjoy")

                return resource_status
            else:
                return "Sorry there is not enough Coffee"
        else:
            return "Sorry there is not enough milk"
    else:
        return "Sorry there is not enough water"


def process_coins():
    q = int(input("How many quarters: "))
    d = int(input("How many dimes: "))
    n = int(input("How many nickels: "))
    p = int(input("How many pennies: "))
    sum_of_coins = q*(coins["Quarter"]/100) +\
              d * (coins["Dime"]/100) +\
              n * (coins["Nickel"]/100) +\
              p * (coins["Penny"]/100)
    return sum_of_coins


def coffee_cost_comparison(coffee_type,coins_sum):
    global coffee
    if coins_sum >= coffee[coffee_type]["Cost"]:
        change = coins_sum - coffee[coffee_type]["Cost"]
        if change>0:
            print(f"Here is your change ${round(change,2)}")
            machine_resources["Water in ml"] -= coffee[coffee_type]["Water in ml"]
            machine_resources["Milk in ml"] -= coffee[coffee_type]["Milk in ml"]
            machine_resources["Coffee in grams"] -= coffee[coffee_type]["Coffee in grams"]
            machine_resources["Cost"] += coffee[coffee_type]["Cost"]
        print(f"Here is your {user_input} '☕'. Enjoy")

    else:
        print("Sorry, insufficient money. Please insert sufficient money. Money Refunded")


def coffee_selected():
    if user_input == "espresso":
        coffee_types = "Espresso"
    elif user_input == "latte":
        coffee_types = "Latte"
    elif user_input == "cappuccino":
        coffee_types = "Cappuccino"
    return coffee_types


def coffee_machine():
    coffee_type = coffee_selected()
    print("Coffee Type", coffee_type)
    if resource_sufficient(coffee_type) == 'OK':
        print("Please enter coins.")
        coins_sum = process_coins()
        print(f"Coins sum {round(coins_sum,2)}")
        coffee_cost_comparison(coffee_type, coins_sum)

    else:
        print(resource_sufficient(coffee_type))




# Ask the user to select a report



machine_status = 'ON'


while machine_status == 'ON':
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        print("Water : ", machine_resources["Water in ml"], "ml", "\n"
              "Milk : ", machine_resources["Milk in ml"], "ml", "\n"
              "Coffee : ", machine_resources["Coffee in grams"], "g", "\n"
              "Cost:", "$", machine_resources["Cost"])
        user_input = input("What would you like? (espresso/latte/cappuccino):  ")
        coffee_machine()
    # if user_input != "report":
    else:
        coffee_machine()






