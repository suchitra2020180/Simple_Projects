## Project 22: Program for silent auction bids.
# Everyone bids silently and at last everyone will know who pays the biggest bid.

# Is there any one to bid : yes or No
#If yes ==> then enter the name and the bidding price
#These names and bid values should form a dictionary 
#Final step is to find the max bidding price

auction_bid={}

user_wish_bidding= "yes"
while user_wish_bidding== "yes":
    new_name=input("Enter your name: ")
    new_bid_price=int(input("Enter the bid price:"))
    auction_bid[new_name]=new_bid_price   ## trick is here
    user_wish_bidding=str.lower(input("Is there any one to bid? :"))

print("List of bidding:",auction_bid)


max=0
for key in auction_bid:
    if auction_bid[key] >max:
        max= auction_bid[key]
        max_quoter_name=key


print(f"The winner is {max_quoter_name} with a bid value of ${max}")

##For highest bid we can also write function as below:
#def highest_bid_details(dict):
    #max=0
    #for key in dict:
        #if dict[key]> max:
            #max= dict[key]
            #max_quoter_name= key

