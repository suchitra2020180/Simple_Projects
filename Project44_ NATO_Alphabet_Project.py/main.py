 #Step1: create a dictionary  such as {letter: word starts with that letter}
 # ASK the user to enter any name
 # then it should the words in phonetic code (means words with all letters in the geneterd name )

import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data.head())
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(new_dict)

entered_str=True
def generate_phonetic():
    name = str.upper(input("Enter a name: "))
    try:
        phonetics = [new_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, Please enter only alphabets")
        generate_phonetic()
    else:
        print(phonetics)

generate_phonetic()