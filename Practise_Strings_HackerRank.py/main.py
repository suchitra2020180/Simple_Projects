##Ques
# S;V;iPad
# C;M;mouse pad
# C;C;code swarm
# S;C;OrangeHighlighter
#ans:
# i pad
# mousePad()
# CodeSwarm
# orange highlighter

def split_comb(input):
    index = []
    input_list = input.split(";")
    if input_list[0] == "S":
        words = input_list[2:]
        if input_list[0] == "V":
            for num in range(0, len(words)):
                if words[num].isupper():
                    index = num
                    print(index)
                    print(words.split(index-1))
    else:
        words = input_list[2:]







input="S;C;OrangeHighlighter"
split_comb(input)
words=input.split(";")
print(words)
print(words[2:])
if words[0]=='S':
    for i in words[2:]:
        print(len(i))
        for j in i:
            if j.isupper():
                index=j
                words_splitted=i.split(j)
                first_word=words_splitted[0]
                sec_word_lower= j.lower()+words_splitted[1]
                result= words_splitted[0]+ " " +sec_word_lower
                print(result)
                if words[1]=="V":
                    print(result)
                elif words[1]=="M":
                    print(result)
                elif words[1]=="C":
                    print("R:",result)
                    for k in result:
                        if k.isupper():
                            print(k)
                            words_splitted = i.split(k)
                            print("LL",words_splitted)
                            print("LL", words_splitted[0])
                            first_word = words_splitted[0]
                            sec_word_lower = k.lower() + words_splitted[1]
                            result = words_splitted[0] + " " + sec_word_lower
                            print("fajhfk==========")
                            print(result)


# input="C;C;code swarm"
# split_comb(input)
# words=input.split(";")
# print(words)
# print(words[2:])
# if words[0]=='C':
#     for i in words[2:]:
#         splitted_words=i.split(' ')
#         print(i.split(' '))
#         first_word =splitted_words[0]
#         sec_word=splitted_words[1]
#         if words[1]=='M':
#             sec_word_up=sec_word[0].upper()
#             mod_sec_word=sec_word[0].upper()+sec_word[1:]
#             result=first_word+mod_sec_word+'()'
#             print(result)
#         elif words[1]=='V':
#             sec_word_up=sec_word[0].upper()
#             mod_sec_word=sec_word[0].upper()+sec_word[1:]
#             result=first_word+mod_sec_word
#             print(result)
#         elif words[1]=='C':
#             sec_word_up=sec_word[0].upper()
#             mod_sec_word=sec_word[0].upper()+sec_word[1:]
#             first_word_up = first_word[0].upper()
#             mod_first_word = first_word[0].upper() + first_word[1:]
#             result=mod_first_word+mod_sec_word
#             print(result)