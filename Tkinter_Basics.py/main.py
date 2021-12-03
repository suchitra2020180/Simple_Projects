import tkinter
from tkinter import *
## Tcl/tk documentation
window = tkinter.Tk()
window.title("My First GUI in Tkinter")
window.minsize(width=500, height=300)
# pading ads space from all four sides
window.config(padx=20, pady=20)
# Initialising label class:
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold" ))
my_label.pack()
#my_label.pack(expand=True)
#my_label.pack(side= "left")
my_label["text"] = "New text"
my_label.config(text="New text")

# Creating buttons
def clicked():
    print("I got clicked")
    #my_label["text"] = "I got clicks"
    new_text = input.get()
    my_label.config(text=new_text)
# BUTTON = tkinter.Button()
button = Button(text="click me", command =clicked)
button.pack()
button.config(padx=20, pady=20)

##Entry

input = Entry(width=10)
input.pack()
print(input.get())

# if we want the typed text to be displayed then use input.get() in my_label and configure

#  text box:
text =Text(width=20, height=10)
# puts cursor in the textbox
text.focus()
# Adds some text to begin with
text.insert(END, "Ex of multiline entry")
# Gets the current value in the textbox at line character 0
print(text.get("1.0", END))
text.pack()

# spin box:
def spin_box():
    # gets the current value from the spin box
    print(spinbox.get())

spinbox=Spinbox(from_=0, to=10, width=5,command =spin_box)
spinbox.pack()


# check button
def check_button():
    # prints 1 if On button checked, otherwise 0
    print(check.get())
# VARIABLE TO HOLD ON CHECK STATE  0 IS OFF AND 1 IS ON
check = IntVar()
checkbutton = Checkbutton(text ="Is On?", variable=check,command=check_button)
check.get()
checkbutton.pack()

# Radio button:

def radio_button():
    # prints 1 if On button checked, otherwise 0
    print(check.get())
# VARIABLE TO HOLD ON CHECK STATE  0 IS OFF AND 1 IS ON
radio = IntVar()
radiobutton1 = Radiobutton(text ="Option1", value=1,variable=radio,command=radio_button)
radiobutton2 = Radiobutton(text ="Option2", value=2,variable=radio,command=radio_button)
radio.get()
radiobutton1.pack()
radiobutton2.pack()

# list box:
def list_box(event):
    # GETS CURRENT SELECTION FROM LIST BOX
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits =["Apple", "Banana", "Pear", "Orange"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", list_box)
#listbox.pack()
listbox.place(x=100, y=10)
#listbox.grid(column=0, row=0)  ## If grid is used then all items should use grid


# grid is easy way and we cannot mix pack() and grid() methods.
# pack will place the item in left or right or centre
# place will place items in our required position



def add(*args):
    sum=0
    for n in args:
        sum += n
    print("Sum:", sum)

add(3, 2, 5)


# Window listens from the user
window.mainloop()