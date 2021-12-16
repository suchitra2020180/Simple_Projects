import numpy as np

def listToMat(l_list):
    l_array=np.asarray(l_list)
    #print(l_array)
    mat = l_array.reshape(3,3)
    return mat

def user1Mat(user1,user1_sel):
    user1_pos = int(input("Player1:Enter a position between 0 to 9: "))
    l_list[user1_pos]= user1_sel
    matrix=listToMat(l_list)
    print(matrix)
    check(user1_sel,matrix,user1)
    #print("checked")
    print(check(user1_sel,matrix,user1))
    return check(user1_sel,matrix,user1)

def user2Mat(user2,user2_sel):
    user2_pos = int(input("Player2:Enter a position between 0 to 9: "))
    l_list[user2_pos]= user2_sel
    matrix=listToMat(l_list)
    print(matrix)
    print(check(user2_sel,matrix,user2))
    return check(user2_sel, matrix, user2)
def check(playerSelectedVariable,mat,user):
    for m in range(0,3):
        if mat[m][0] == playerSelectedVariable and mat[m][1] == playerSelectedVariable and mat[m][2] == playerSelectedVariable:
            return f"{user} is the winner"
        elif mat[0][m] == playerSelectedVariable and mat[1][m] == playerSelectedVariable and mat[2][m] == playerSelectedVariable:
            return f"{user} is the winner"
        elif mat[0][0] == playerSelectedVariable and mat[1][1] == playerSelectedVariable and mat[2][2] == playerSelectedVariable:
            return f"{user} is the winner"
        elif mat[2][0] == playerSelectedVariable and mat[1][1] == playerSelectedVariable and mat[0][2] == playerSelectedVariable:
            return f"{user} is the winner"
        else:
            return "No match"
# def checkAns(playerSelectedVariable,mat,user):
#     if mat[0][0]==playerSelectedVariable and mat[0][1]==playerSelectedVariable and mat[0][2]==playerSelectedVariable:
#         #print(f"{playerSelectedVariable} is winner")
#         return f"{user} is the winner"
#
#     elif mat[1][0]==playerSelectedVariable and mat[1][1]==playerSelectedVariable and mat[1][2]==playerSelectedVariable:
#         return f"{user} is the winner"
#
#     elif mat[2][0]==playerSelectedVariable and mat[2][1]==playerSelectedVariable and mat[2][2]==playerSelectedVariable:
#         return f"{user} is the winner"
#     elif mat[0][0]==playerSelectedVariable and mat[1][0]==playerSelectedVariable and mat[2][0]==playerSelectedVariable:
#         return f"{user} is the winner"
#     elif mat[0][1]==playerSelectedVariable and mat[1][1]==playerSelectedVariable and mat[2][1]==playerSelectedVariable:
#         return f"{user} is the winner"
#     elif mat[0][2]==playerSelectedVariable and mat[1][2]==playerSelectedVariable and mat[2][2]==playerSelectedVariable:
#         return f"{user} is the winner"
#     elif mat[2][0]==playerSelectedVariable and mat[1][1]==playerSelectedVariable and mat[0][2]==playerSelectedVariable:
#         return f"{user} is the winner"
#     elif mat[0][0]==playerSelectedVariable and mat[1][1]==playerSelectedVariable and mat[2][2]==playerSelectedVariable:
#         return f"{user} is the winner"
#     else:
#         return "No match"

print("Welcome to TicTac Game")
user1=input("Enter the name of player1: ")
user1_sel=(input("Select any character from A-Z: ")).upper()

user2=input("Enter the name of player2: ")
user2_sel=input(f"Select any character from A-Z .User1 selected {user1_sel}: ").upper()

if user1_sel ==user2_sel:
    print(f"Player1 already selected {user1_sel}")
    user2_sel =input(f"Please select a character from A-Z except {user1_sel}: ").upper()
else:
    l_list = ['x' for i in range(0, 9)]
    l_array = np.asarray(l_list)
    mat = l_array.reshape(3, 3)
    # print(mat)
    #print(listToMat())
    count=0
    continueGame = 'yes'
    while count < 9 and continueGame =="yes":
        if count ==8:
            print("Draw GAME")
            # print("END OF THE GAME")
            continueGame = 'No'

        #user1Mat(user1, user1_sel)
        user1_res=user1Mat(user1, user1_sel)
        print("User1 Result:",user1_res)
        if user1_res =="No match":
            count =count+1
        elif user1_res ==f"{user1} is the winner":
            print(f"{user1} WON THE GAME")
            break

        user2_res =user2Mat(user2, user2_sel)
        #print("User2 Result:", user2_res)
        if user2_res =="No match":
            count = count +1
        elif user2_res == f"{user2} is the winner":
            print(f"{user2} WON THE GAME")
            break


    print("END OF THE GAME")
