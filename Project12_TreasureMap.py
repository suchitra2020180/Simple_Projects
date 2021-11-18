##Project12:  Treasure map using emojis
#Get emojis from:   https://getemoji.com/ 
##Make 3 rows of emojis and list them.Then make a matrx and using index find the treasure

row1=['😄', '😁', '😆']
row2=['😏','😒', '😞']
row3=['😈','🤑','😎']
#treasure='🤑'
combine_rows=[row1,row2,row3]
print(combine_rows)
print(f"{row1}\n,{row2}\n,{row3}\n")
##FINDING TREASURE
row_t=2
col_t=1
Treasure=combine_rows[row_t][col_t]
row=int(input("Enter row number to find treasure:"))
col=int(input("Enter column number to find treasure:"))
emoji=combine_rows[row][col]

if (row==row_t and col==col_t):
    print(f"Alas !! You found treasure {Treasure}")
    treasure_position=input("Would you like to shift the position of the treasure?- type Y if YES and N for NO:  ")
    if treasure_position=='Y':
        row_pos=int(input("Which row would you like to choose for treasure: "))
        col_pos=int(input("Which column would you like to choose for treasure: "))
        exist_emoji=combine_rows[row_pos][col_pos]
        combine_rows[row_pos][col_pos]= Treasure
        combine_rows[row_t][col_t]=exist_emoji
        print(combine_rows)
else:
    print(f" Sorry, You found {emoji}")


