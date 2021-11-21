#### Project :28 BlackJack program or 21 game
## card eith jack, queen,king (J,Q,K) willhave value of 10. But ACE (A) can have a value of 1 or 11.Depending on the sum u can decide the value.
##Remember if ur sum >21 u lose
#CARDS START FROM 2 TO 10
## Hit play and click deal then the deal will give some cards.
## If both players have sum <21 then click deal to get some card. If the sum is <17 then the dealer must take a card
##If the sum of cards =21 you will win or u will lose. iF SUM >21 THEN LOSE
#Cards Description: 
##Total cards=52
# 4 sets of cards -Heart, dimond, spade and club.
# Each set have 13 cards=[A, 2, 3,4 ,5 6,7,8, 9, 10,J, Q,K]
# A is ACE and can have value of 1 or 11.
# J is JACK, Q -Queen, K-King and J,Q,K have a face value of 10
## Here we assume equal probablity of occuring each card.
## Cards are not removed from the deck  as they are drawn.

import random
game=str.upper(input("Do you want to play a game of blackjack? Type Y for yes and N for no: "))
#from ascii_logos import blackjack_logo
#print(blackjack_logo)
game='Y'
if game=='Y':
    #from ascii_logos import blackjack_logo
    #print(blackjack_logo)
    A=11
    J=10
    Q=10
    K=10
    #cards=['A', 2, 3,4 ,5, 6,7,8, 9, 10,'J','Q','K']
    cards=[11, 2, 3,4 ,5, 6,7,8, 9, 10,10,10,10]
    your_cards=[]
    computer_cards=[]
    your_card_sum=0
    computer_card_sum=0
    for i in range(0,2):
        your_selected_cards=random.choice(cards)
        your_cards.append(your_selected_cards)
        computer_choice=random.choice(cards)
        computer_cards.append(computer_choice)
        
    
    
    for i in range(0,len(your_cards)):
        your_card_sum += your_cards[i]
    print(f"{your_cards} Your card sum is {your_card_sum}")
    print([computer_cards[0], 'x'])
    for i in range(0, len(computer_cards)):
        computer_card_sum += computer_cards[i]
        print(computer_card_sum)

    if your_card_sum < 17:
        your_input=str.upper(input("Want to pick one more card?- 'Y' for Yes and 'N' for No "))
        if your_input=='Y':
            your_selected_cards=random.choice(cards)
            your_cards.append(your_selected_cards)
    if computer_card_sum < 17:
        print("Computer picked a card.")
        computer_selected_cards=random.choice(cards)
        computer_cards.append(your_selected_cards)
        your_card_sum=0
        computer_card_sum=0
    for i in your_cards:
        your_card_sum += i
    for i in computer_cards:
        computer_card_sum += i
    print(f"{your_cards} Your cards sum is {your_card_sum}")
    print(f"{computer_cards} Computer card sum is {computer_card_sum}")

    if your_card_sum > 21:
        print("You lose")
    elif computer_card_sum >21:
        print("Computer lose and You won")
    elif (your_card_sum > computer_card_sum and your_card_sum  <=21):
        print("You won")


