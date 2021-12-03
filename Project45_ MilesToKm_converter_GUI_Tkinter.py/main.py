
import tkinter
from tkinter import *

# Window settings
window = tkinter.Tk()
window.title("Miles to Kilometer converter")
window.minsize(width=100, height=100)
window.config(padx=30, pady=30) # 30 pixels padding is given


# To allow user to take input in miles
Input = Entry(width=10)
#Input.pack()
print(Input.get())
Input.grid(column=1, row=0)


# Creating calculate button
def button_work():
    miles = Input.get()
    # Converting miles to km
    Km = round(float(miles) * 1.60934)
    #Output["text"] = Km
    Output.config(text=Km)


calculate_button = Button(text="Calculate", command=button_work)
calculate_button.grid(column=1, row=2)

# To display output in Km
Text = 0
Output = tkinter.Label(text=Text, font=("Arial", 12))
Output.grid(column=1, row=1)


# Labels in window
m_label = tkinter.Label(text="Miles", font= ("Arial", 12))
m_label.grid(column=2, row= 0)
km_label = tkinter.Label(text="Km", font= ("Arial", 12))
km_label.grid(column=2, row=1 )
text_label = tkinter.Label(text="is equal to", font=("Arial", 12))
text_label.grid(column=0, row= 1)

window.mainloop()
