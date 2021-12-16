
import numpy as np
print("Welcome to TicTac Game")
filled_pos = []
a=np.zeros(9)
print(a[0])

array = np.zeros(9)
print("Array:", array)
list=[]
for i in range(0,9):
    list.append('0')
array_list = np.asarray(list)
mat = array_list.reshape(3, 3)
print("Matrix:", mat)


user1=input("Enter the name of player1: ")
user1_sel=(input("Select any character from A-Z: ")).upper()

user2=input("Enter the name of player2: ")
user2_sel=(input(f"Select any character from A-Z .User1 selected {user1_sel}: ")).upper()
def arr_to_mat(list):
   # global list
    #array = np.zeros(9)
    #print("Array:", array)
    array_list=np.asarray(list)
    mat = array_list.reshape(3, 3)
    print("Matrix:", mat)
    print("Done sECOND step:",mat)
    checkAns(user1_sel)
    checkAns(user2_sel)
    #return mat

def win_condition(mat):
    #global mat
    print("Step3")
    for m in range(0,3):
        if mat[m][0]==mat[m][1] and mat[m][1]==mat[m][2]:
            print("You won")
        elif mat[0][m]==mat[1][m] and mat[1][m]==mat[2][m]:
            print("You won")
        elif mat[0][0]==mat[1][1] and mat[1][1]==mat[2][2]:
            print("You won")
        elif mat[0][2]==mat[1][1] and mat[1][1]==mat[2][2]:
            print("You won")
        else:
            user_entry()

def checkAns(playerSelectedVariable):
    if mat[0][0]==playerSelectedVariable and mat[0][1]==playerSelectedVariable and mat[0][2]==playerSelectedVariable:
        return playerSelectedVariable + "is winner"
    elif mat[1][0]==playerSelectedVariable and mat[1][1]==playerSelectedVariable and mat[1][2]==playerSelectedVariable:
        return "playerSelectedVariable is winner"
    elif mat[2][0]==playerSelectedVariable and mat[2][1]==playerSelectedVariable and mat[2][2]==playerSelectedVariable:
        return "playerSelectedVariable is winner"
    elif mat[0][0]==playerSelectedVariable and mat[1][0]==playerSelectedVariable and mat[2][0]==playerSelectedVariable:
        return "playerSelectedVariable is winner"
    elif mat[0][1]==playerSelectedVariable and mat[1][1]==playerSelectedVariable and mat[2][1]==playerSelectedVariable:
        return "playerSelectedVariable is winner"
    elif mat[0][2]==playerSelectedVariable and mat[1][2]==playerSelectedVariable and mat[2][2]==playerSelectedVariable:
        return "playerSelectedVariable is winner"
    elif mat[2][0]==playerSelectedVariable and mat[1][1]==playerSelectedVariable and mat[0][2]==playerSelectedVariable:
        return "playerSelectedVariable is winner"
    elif mat[0][0]==playerSelectedVariable and mat[1][1]==playerSelectedVariable and mat[2][2]==playerSelectedVariable:
        return "playerSelectedVariable is winner"
    # else:
    #     user2()



def user2():
    user2_pos = int(input("Player2: Enter the position between 0 to 8: "))
    list[user2_pos] = user2_sel
    print("Done first step:", list)
    filled_pos.append(user2_pos)

def user_entry():
    global filled_pos
    user1_pos=int(input("Player1: Enter the position between 0 to 8: "))
    print("Array list:",array_list)
    list[user1_pos] = user1_sel
    print(list)
    filled_pos.append(user1_pos)
    arr_to_mat(filled_pos)
    checkAns(user1_sel)

    user2_pos=int(input("Player2: Enter the position between 0 to 8: "))
    list[user2_pos] = user2_sel
    print("Done first step:",list)
    filled_pos.append(user2_pos)
    print("Filled positions:",filled_pos)
    arr_to_mat(filled_pos)
    checkAns(user2_sel)
    #return list

    #mat=np.zeros((3,3))


    array = np.zeros(9)
    for i in range(0,9):
        list = user_entry()
        arr_to_mat(list)
        # print(mat[0])
        # if mat[0][0]== mat[0][2]:
        #     print("Match")
        ###checkAns(user1_sel)
        #win_condition(mat)
        #win_condition(arr_to_mat(user_entry))


