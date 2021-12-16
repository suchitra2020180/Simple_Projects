from data import question_data
data =question_data
for i in range(0,len(data)):
    q = data[i]['text'].replace(, '?')

    print(f"{q},{len(q)}")