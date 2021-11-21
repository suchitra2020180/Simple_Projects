##Project18: Guessing a word

### STEP1: Select a word randomly from words_list and place it in choosen word.
## STEP2: Ask the user to guess a letter and place it in another variable (guess)
## STEP3: Check the letter guessed by user is in the word or not
## STEP4: Count the number of letter in choosen word and create blankspaces list  called display, with same  count
## STEP5: Replace the blank list with the guess letter if guess is correct
## STEP6: Write a loop to guess a letter until the display is complete.
#STEP 7: Create a variable called lives to store the lives left
#STEP8: Set Lives=6
#STEP9:  Write a program such that if the guess is wrong then the lives will be reduce by 1. 
# If Lives reaches 0 the game should stop and print "YOU LOSE"
#STEP 10: Join all the letters in the output to make a string.
#3STEP 11: PRINT ascii art if possible

print(''' Welcome to 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     ''' )
import random
words_list=["ardvark","baboon", "camel","yourself","strong","belief", "building"]
choosen_word=str.lower( random.choice(words_list))
#print("Choosen word:",choosen_word)

display=[]
for i in range(0,len(choosen_word)):
    display.append('_')
print(display)
d_count=display.count('_')
print("No. of blanks:",d_count)
lives=7
print(" Lives given:",lives)
stages=[
 '''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\\
     |
 jgs_|___ ''',
  '''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 jgs_|___''',
 '''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
 jgs_|___''',
  '''
       _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 jgs_|___''',
  '''
       _______
     |/      |
     |      (_)
     |      \|
     |       
     |       
     |
 jgs_|___''',
  '''
       _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
 jgs_|___''',
 '''  
  _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 jgs_|___''',
 ]

guessed_list=[]
while (d_count>0 and lives >0):
    guess=str.lower(input("Guess a letter: "))
#print("Guess letter:", guess)
    
    if guess in guessed_list:
        print("Already guessed the letter")
    guessed_list.append(guess)

    for position in range(0,len(choosen_word)):
        if choosen_word[position]==guess:
            display[position]=guess
            d_count=display.count('_')

        
    if guess not in choosen_word:
        lives -=1
        print("Guess letter is not in word and lives left:",lives)
        print(stages[lives])
        if lives ==0:
            print("You Lose")
    print(display)
if d_count==0:  
    print("You WON")    


#for letter in choosen_word:
   # if letter== guess:
        #print("Your Guess is correct")
   # else:
      #  print("Your Guess is wrong")