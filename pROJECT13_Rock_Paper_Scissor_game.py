###  Project13: Rock, Paper,Scissor game

##Ask the user to choose 0 for Rock, 1 for Paper and 2 for Scissor.
##Computer will randomly choose any one from Rock, paper and Scissor.
#If both choices match then you will win or else you will lose.
import random
#elements=['Rock','Paper','Scissor']
elements=['''  ____, O
   /   /M|
  /|MMMMMMMM
  {| | // |}
-_}| |/ \ |{_apx ''','''  _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|       ''','''   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/''']
user_selected=int(input("What is your choice 0 for Rock, 1 for Paper and 2 for Scissor: "))

if (user_selected <=3):
    user_input=elements[user_selected]
    print("User input: ", user_input)
    computer_selected=random.randint(0,2)
    computer_input=elements[computer_selected]
    print("Computer selected: ", computer_input)

    if user_selected==computer_selected:
        print('Its a draw')
    elif (user_selected==2 and computer_selected==0):
        print("You lose")
    elif (user_selected==0 and computer_selected==2):
        print("You won the game 😀")
    elif (user_selected > computer_selected): 
        print("You won the game 😀")
    else:
        print('You LOSE 😭')
else :
    print("Please rerun the program and enter a number between 0 and 3 and")