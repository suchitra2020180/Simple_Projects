### Project 29: Number_Guessing_Game
## Step1: Computer will guess a number between 1 to 100
##Ask the user for the level of difficulty
# Easy level will have 10 attempts and hard level will have 5 attempts.
##If the user entered number is greater than computer guess number, then print "Too high" else print "Too low".
##Let the user repeat the steps until, the user guess the correct answer, for the selected attempts.
#If attempts are completed then stop the game.


import random
#import numpy as np
logo=''' _______               ___.                     ________                              
 \      \  __ __  _____\_ |__   ___________    /  _____/ __ __   ____   ______ ______ 
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \  /   \  ___|  |  \_/ __ \ /  ___//  ___/ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/  \    \_\  \  |  /\  ___/ \___ \ \___ \  
\____|__  /____/|__|_|  /___  /\___  >__|      \______  /____/  \___  >____  >____  > 
        \/            \/    \/     \/                 \/            \/     \/     \/  '''

def comparison(computer_selected,attempts):
    user_guess=int(input("Make a guess: "))
    while attempts > 0:
        if user_guess==computer_selected:
            print(f"You got it! The answer was {computer_selected}")
            play_again=str.upper(input("Want to play again: 'Y' OR 'N'"))
            if play_again=='Y':
                Number_Guess_Game()
            else:
                print("Good Luck")
                
        elif user_guess > computer_selected:
            attempts -=1
            print("Too high")
            if attempts >0:
                print(f"You have {attempts} attempts remaining to guess a number")
                print("Guess Again")
                user_guess=int(input("Make a guess: "))
            else:
                print("You Lose")
        else:
            attempts -=1
            print("Too low")
            if attempts >0:
                print(f"You have {attempts} attempts remaining to guess a number")
                print("Guess Again")
                user_guess=int(input("Make a guess: "))
            else:
                print("You Lose")


def Number_Guess_Game():
    print(logo)
    print(" Welcome to the Number Guessing Game !!")
    print("I am thinking of a number between 1 to 100.")
    numbers=range(1,100,1)
    level=input("Choose a level of difficulty. Type 'easy' or 'hard': ")        
    computer_selected=random.choice(numbers)
    print(computer_selected)
    
    if level=='easy':
        attempts=10
        print(f"You have {attempts} attempts remaining to guess the number")
        comparison(computer_selected,attempts)
        #easy()
    else:
        attempts=5
        print(f"You have {attempts} attempts remaining to guess the number")
        comparison(computer_selected,attempts)
        #hard()


##Play the
Number_Guess_Game()