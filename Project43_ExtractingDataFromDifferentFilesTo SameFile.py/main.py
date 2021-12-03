with open("file1.txt") as f1:
    f1_cont = f1.read()
    F1 = f1_cont.split("\n")
    print(F1)

with open("file2.txt") as f2:
    f2_cont = f2.read()
    print(f2_cont)
    F2 = f2_cont.split("\n")
    print(F2)

common_data = [i for i in F1 if i in F2]
print(f"COMMON DATA: {common_data}")


######
import random
names = ["Alex", "maddy", "sandy"]
new_dict = {stu:random.randint(1, 100) for stu in names}
print(new_dict)
passed_stu = {stu:score for (stu,score) in new_dict.items() if score >=60}
print(passed_stu)

## Counting number of letters in each word
sentence ="What is python?"
words = sentence.split(" ")
print(words)
word_dict = {word: len(word) for word in words}
print(word_dict)

# performing mathematical operation on each value of the word_dict dictionary
word_dict2 = {word: value*2+3 for (word,value) in word_dict.items()}
print(word_dict2)