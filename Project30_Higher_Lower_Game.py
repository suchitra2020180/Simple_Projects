###Project 30: Higher Lower Game
#steps: Compare A and B. Play until you lose and then it prints your score


import random


def highest_value(A,B):
    #highest_followers=0
    if A['follower_count'] > B['follower_count']:
        highest_followers='A'
    else:
        highest_followers='B'
    return highest_followers



def Higher_Lower_Game(A,data):
    global score
    B=random.choice(data)
    if A==B:
        B=random.choice(data)
        
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print("vs")
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")
    #print(data[0])
    ''' For checking purpose'''
    A_followers=A['follower_count']
    B_followers=B['follower_count']
    print('A score:',A_followers)
    print('B score:',B_followers)
    ''' ============================'''
    user_guess=str.upper(input("Guess who has more followers? Type 'A' or 'B': "))
    
    print('user guess:',user_guess)
    print('highest_value:',highest_value(A,B))
    if user_guess==highest_value(A,B):
        score = score+ 1
        print("score",score)
        print(f"You are right !     Current score is {score}")
        print("==============Next game=============")
        A=B
        Higher_Lower_Game(A,data)


    else:# user_guess!=highest_value(A,B)
        print(f"You are wrong and your final score is {score}")

##Play game here
print("Welcome to Higher Lower Vs Game!!!")
from Project30_GameData import data
A=random.choice(data)
score=0
Higher_Lower_Game(A,data)
