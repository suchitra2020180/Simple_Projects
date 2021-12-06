import tkinter
from tkinter import *
import pandas as pd


#-------------------------Reading data from file=======================#
import random
current_card = {}
to_learn={}
try:
    data = pd.read_csv("Language_Translator_Sheet1.csv")
except:
    original_data = pd.read_csv("Words_to_learn.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pd.DataFrame(to_learn)
    data.to_csv("Words_to_learn.csv", index=False)
    next_card()


# ===-------------------------------- UI Design------------------------------- #


window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg="light green")

flip_timer = window.after(3000, func=flip_card)



canvas = Canvas(width=800, height=526)
#canvas.itemconfig(padx=50, pady=50)
#canvas.create_rectangle(80, 0, 80, 0, fill='light green')
back_card = PhotoImage("card_back.png")
front_card = PhotoImage("card_front.png")

#canvas.create_image(100, 100, image=front_card)
card_background = canvas.create_image(400, 263, image=back_card)
card_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg="#B100C6", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_icon = PhotoImage("check_tick.png")
r_button = Button(width=8, height=5, text="right_icon", highlightthickness=0,  command=is_known, bg="green")
r_button.config(padx=50, pady=50)
r_button.grid(row=1, column=1)

wrong_icon = PhotoImage("wrong.png")
#w_button = Button(image=wrong_icon, highlightthickness=0, width=50, height=50,  command=next_card)
w_button = Button(text="wrong_icon", highlightthickness=0, width=8, height=5,  command=next_card,bg="red")
w_button.config(padx=50, pady=50)
w_button.grid(row=1, column=0)

#canvas.create_text(200, 100, text="French", font="Italic")
#canvas.create_text(200, 200, text="French", font="Times 20 italic bold")

next_card()

window.mainloop()