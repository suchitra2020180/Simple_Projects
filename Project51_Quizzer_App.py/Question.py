class Question():
    def __init__(self, text, ans):
        self.ques = text
        self.ans = ans

window = tkinter.Tk()
window.title("Quizzer")
window.geometry("1500x800")


score_label = Label(text=f"Score:{score}", font=("Arial", 18, "bold"))
score_label.grid(row=0, column=2)

canvas = Canvas(width=900, height=500, bg="blue")
# syntax: create_rectangle(x, y , x+width, y+height)
quiz_board = canvas.create_rectangle(50, 100, 800, 350, fill="yellow", width=5)
quiz_q = canvas.create_text(400, 200, text=current_question, font=("Arial", 16), width=750)
canvas.grid(row=1, column=1)

R_button = Button(text="R", font=("Arial", 24, "bold"), fg="white", bg="green", command=correct)
R_button.grid(row=2, column=0)
W_button = Button(text="x", font=("Arial", 24, "bold"), fg="white", bg="red", command=wrong)
W_button.grid(row=2, column=2)



window.after(5000, func=next_question)

window.mainloop()
score = 0
ques_num = 0
for i in range(0, len(q_list)):
    q = html.unescape(q_list[i]["question"])
    a = q_list[i]["answer"]
    print("ans:",a)
    user_ans= input(f"Q.{ques_num+1}:{q} (True/False):")

    if user_ans ==a:
        print("You got right")
        score +=1
        print(f"Score:{score}/{ques_num+1}")
    else:
        print("Sorry")
        print(f"Score:{score}/{ques_num + 1}")
    ques_num +=1