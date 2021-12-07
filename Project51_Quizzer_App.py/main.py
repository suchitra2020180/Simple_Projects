# Get data from Trivia data base  (https://opentdb.com/api_config.php)
# Create a dictionary
# Create a quiz card with right and wrong icons

import requests
import tkinter
from tkinter import *
import time
#html is imported to convert the unreadable text to readable ones
import html

quiz_board_color="white"
canvas_color = "#CAFF70"
# ----------------------------------------Creating questions for quiz -----------------------------------#
parameters = {"amount": 10,
             "type": "boolean"
             }
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
#response = requests.get(url="https://opentdb.com/api.php?amount=10&category=22&difficulty=medium&type=boolean")
# chck if there are any exceptions
print(response.raise_for_status())
# Check the status code
print(response.status_code)
# Retrieve the data in json
data = response.json()
print(data)
###Keys in data
print(data['results'])
result = data['results']
catt = data['results'][0]['category']
print(catt)

# Creating list of questions
q_list = []
for item in range(0, len(result)):
    print("Item:", result[item])
    print("Question:", result[item]['question'])
    ques = result[item]['question']
    ans = result[item]['correct_answer']
    d = {"question": ques, "answer": ans}
    print(d)
    q_list.append(d)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("q_list:", q_list)
print("q_list_fist_element:", q_list[0])
print("q_list_fist_ques_element:", q_list[0]["question"])
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

# ------------------------------------------------------- Working of buttons
q_no=0
current=0
current_question = html.unescape(q_list[current]["question"])
current_ans = q_list[current]["answer"]
#c_ques = Question(current_question,current_ans)
def next_question():
    global current, q_no
    if current == len(q_list) and q_no == len(q_list):
        # Once the user reaches end of quiz the check should not work
        R_button.config(stat="disabled")
        W_button.config(stat="disabled")
        Next_q_button.config(stat="disabled")
    canvas.itemconfig(quiz_board, fill=quiz_board_color)
    try:
        if current < len(q_list) and q_no < len(q_list):
            current += 1
            q_no += 1
            q_no_label.config(text=f"Q.No: {q_no+1}")
            current_question = html.unescape(q_list[current]["question"])
            current_ans = q_list[current]["answer"]
    except IndexError:
        canvas.itemconfig(quiz_q, text="QUIZ COMPLETED")
        print("QUIZ COMPLETED")
    else:
        canvas.itemconfig(quiz_q, text=current_question)


score = 0
def correct():
    global score, current_ans
    user_ans = "True"
    if user_ans == current_ans:
        canvas.itemconfig(quiz_board, fill="green")
        score += 1
        score_label.config(text=f"Score: {score}")
        #window.after(50000, func=next_question)
    else:
        canvas.itemconfig(quiz_board, fill="red")
        #window.after(50000, func=next_question)
    #timer = window.after(1000, func=next_question)



def wrong():
    global score, current_ans
    user_ans = "False"
    if user_ans ==current_ans:
        canvas.itemconfig(quiz_board, fill="green")
        score += 1
        score_label.config(text=f"Score: {score}")
        #window.after(50000, func=next_question)
    else:
        canvas.itemconfig(quiz_board, fill="red")
        #window.after(50000, func=next_question)
    #timer = window.after(1000, func=next_question)



# -------------------------------------UI Design --------------------------------
window = tkinter.Tk()
while current < 11:
    print("Current:",current)

    window.title("Quizzer")
    window.geometry("1150x700")
    window.config(padx=20, pady=20, bg="#375263")
    #window.after(5000, func=next_question)

    score_label = Label(text=f"Score:{score}", font=("Arial", 18, "bold"), bg="#375263", fg="white")
    score_label.grid(row=0, column=2)

    q_no_label = Label(text=f"Q.No:{q_no+1}", font=("Arial", 18, "bold"), bg="#375263", fg="white")
    q_no_label.grid(row=0, column=0)

    canvas = Canvas(width=900, height=500, bg=canvas_color)
    # syntax: create_rectangle(x, y , x+width, y+height)
    quiz_board = canvas.create_rectangle(50, 100, 800, 350, fill=quiz_board_color, width=5)
    quiz_q = canvas.create_text(450, 200,  text=current_question, font=("Arial", 16), width=700)
    #canvas.itemconfig(padx=50, pady=50)
    canvas.grid(row=1, column=1, pady=20)

    R_button = Button(text="✔", font=("Arial", 24, "bold"), fg="white", bg="green", command=correct)
    R_button.grid(row=2, column=0)
    W_button = Button(text="✘", font=("Arial", 24, "bold"), fg="white", bg="red", command=wrong)
    W_button.grid(row=2, column=2)

    Next_q_button = Button(text="Next Question", font=("Arial", 24, "bold"), fg="white", bg="cyan", command=next_question)
    Next_q_button.grid(row=2, column=1)


    window.mainloop()
