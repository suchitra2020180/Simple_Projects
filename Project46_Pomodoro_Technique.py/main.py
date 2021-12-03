import tkinter
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer= None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_fun():
    window.after_cancel(timer)
    canvas.itemconfig(timer, text="00:00")
    Title_label.config(text=timer)
    check_marks.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
# Tkinter displays in millisec
def start_fun():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    count_down(work_sec)
    # 1 min=60
    #Minutes= total_sec/60

    # if its the 8th repetation:
    if reps % 8==0:
        count_down(long_break_sec)
        Title_label.config(text="Long break", fg=RED)
    # if its the  2nd/4th/6th repetation:
    elif reps %2 ==0:
        count_down(short_break_sec)
        Title_label.config(text="SHORT break", fg=PINK)
    else:
        count_down(work_sec)
        Title_label.config(text="WORK", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
# time.sleep(1)  # sleep for a second
def count_down(count):
    # floor gives the largest whole number i.e, 4 from 4.50
    count_min = math.floor(count/60)  ##quotient
    count_sec = count % 60  ## remainder
    if count_sec < 10:
        count_sec= f"0{count_sec}"
    # CHANGING LABEL IN CANVAS
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1) # Here count-1 is passed into the count_down() after 1000milliseconds
    else:
        start_fun()
        #reps = 4
        mark = ""
        work_sessions =math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)

##After sometime it calls a function

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


##Forinserting images use canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # Tomato diemnsions
# removing the border line of image
Tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=Tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)





Title_label = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg =YELLOW)
Title_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_fun,  highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_fun, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)


window.mainloop()
