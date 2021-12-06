# Once the password is generated use pyperclick package to copy and paste it in website



import tkinter
from tkinter import *
import random
import string
from tkinter import messagebox, Entry
import pyperclip
import json
#------------------------------------Password Generator--------------------------------------


def password_generation():
    symbols = ["@", "#", "$", "%", "&", "*"]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lower_case_letters = list(string.ascii_lowercase)
    upper_case_letters = list(string.ascii_uppercase)
    sym_for_pw = [random.choice(symbols) for sym in range(0, 3)]
    num_for_pw = [random.choice(numbers) for num in range(0, 3)]
    lower_letter_for_pw =[random.choice(lower_case_letters) for low_let in range(0, 3)]
    upper_letter_for_pw = [random.choice(upper_case_letters) for upp_let in range(0, 3)]
    pw = sym_for_pw+num_for_pw+lower_letter_for_pw+upper_letter_for_pw
    print(pw)
    random.shuffle(pw)
    # password = ""
    ##for i in range(0, len(pw)):
        #password += pw[i]
    #print(password)

    password= "".join(pw)
    print(password)
    Password_input.insert(0, password)
    pyperclip.copy(password) # when this command run it already copies the password abnd we can paste it anywhere

# ------------------------------------- Save details to a file--------------------------------
def adding():

    website = website_input.get()
    pass_word =Password_input.get()
    email = Email_input.get()
    new_data = {
        website:{
            "email": email,
            "password": pass_word

        }


    }
    # Creating popup to confirm the details for saving to a file
   # messagebox.showinfo(title="Title", message="Confirm the Details")
    messagebox.askokcancel(title=website, message=f"These are the details entered:Website:{website}, Email:{email}, Password:{pass_word}")
    # Append the email, password and website data entered by user

    if len(website)==0 or len(pass_word)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty")
    else:
        try:
            with open("Password_saver.json", "r") as file:
                # Reading the old data from file
                data = json.load(file)
        except FileNotFoundError:
            with open("Password_saver.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # update the daa
            data.update(new_data)
            with open("Password_saver.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            # After adding the details reset all the fields
            website_input.delete(0, END)
            # Email_input.delete(0, END) # We want this to stay on email
            Password_input.delete(0, END)




#----------------------------------Search function-----------#
def search_fun():
    try:
        with open("Password_saver.json", "r") as file:
            # Reading the old data from file
            data = json.load(file)

    except FileNotFoundError:
        with open("Password_saver.json", "w") as file:
            json.dump(new_data, file, indent=4)

    else:
        if website_input.get() in data:
            messagebox.showinfo(title=website_input.get(), message=f"Password: {data[website_input.get()]['password']}")
        else:
            messagebox.showinfo(title=website_input.get(), message="No record found")

            #print(data[web])
            #print(web)
            #print(value['password'])
            #print(data[web][value])



# ----------------------------------------- UI setup --------------------------------------------

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=400, height=400, bg="red")
password_image = PhotoImage(file="password_Image.png")
canvas.create_image(200, 200, image=password_image)
#canvas.itemconfig(padx=20, pady=20)
canvas.grid(column=1, row=0)

# use columnspan to go over multiple rows
website_label = Label(text="Website:", font=("Arial", 16), bg="white")
website_label.grid(column=0, row=1)

Email_label = Label(text="Email:", font=("Arial", 16), bg="white")
Email_label.grid(column=0, row=2)

Password_label = Label(text="Password:", font=("Arial", 16), bg="white")
Password_label.grid(column=0, row=3)

website_input: Entry = Entry(width=21)
website_input.grid(column=1, row=1) # COLUMNSPAN=2
website_input.focus()
website_input.get()

search_button = Button(text="Search", command=search_fun, bg="white", width=13)
search_button.grid(column=2, row=1)

Email_input = Entry(width=35)
# tO DISPLAY A FIRST NAME # 0 is index
Email_input.insert(0, "suchitraraniojha@gmail.com")
Email_input.grid(column=1, row=2, columnspan=2)
Email_input.get()

Text = "Password"
#Password_input = Label(width=21, text=Text, font=("Arial", 16), bg="white")
Password_input = Entry(width=21)
Password_input.grid(column=1, row=3)
Password_input.focus()
#Password_input.insert(0,f"{password}")



generate_pw_button = Button(text="Generate Password", command=password_generation, bg="white")
generate_pw_button.grid(column=2, row=3)

Add_button = Button(width=36, text="Add", command=adding)
Add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
