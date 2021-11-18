##pROJECT 8: LOVE CALCULATOR
##Enter names of two persons
##Count the number the times the letters in TRUE LOVE appears in both names
##sum the count of TRUE and then count OF LOVE
#If TRUE count is 6 and LOVE count is 3 then the compatability is 63%

print("=== Welcome to love calculator ===")
person1=str.lower(input("Enter your name: "))
person2=str.lower(input("Enter another name with whom yo want to see the compatibilty: "))
persons=[person1,person2]
ref_word1=str.lower("TRUE")
ref_word2=str.lower("LOVE")

### splitting the caracters in person1 and person2
char_list=[]
for i in persons:
    for j in i:
        char_list.append(j)
print(char_list)

## splitting the characters in ref_words
word1_list=[]
ref_word1_list=[i for i in ref_word1]
ref_word2_list=[i for i in ref_word2]
print(ref_word1_list)
print(ref_word2_list)

##Counting the number of times, the characters in persons are repeated in ref_words
TRUE_count=0
for i in char_list:
    for j in ref_word1_list:
        if i==j:
            TRUE_count += 1
    print(f"{j} appears  {TRUE_count} times")
        

LOVE_count=0
for i in char_list:
    for j in ref_word2_list:
        if i==j:
            LOVE_count += 1
    print(f"{j} appears  {LOVE_count} times")

#print("TRUE Count:", TRUE_count)
#print("LOVE Count:", LOVE_count)


##Calculating LOVE_SCORE
Love_score= TRUE_count*10 + LOVE_count
#print(f"Love score of  {person1} and {person2} is {Love_score}")

if (Love_score < 10 or Love_score > 90):
    print(f"Your score is {Love_score}, you go together like coke and mentos")
elif (Love_score > 40 and Love_score < 50):
    print(f"Your score is {Love_score}, you are alright together")
else:
    print(f"Your score is {Love_score}")

