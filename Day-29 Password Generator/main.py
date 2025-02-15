from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
from IPython.utils.text import columnize
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    # JOIN method
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():

    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website :{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not make any fields empty")
    else: 
            try:    
                with open("passwords.json", "r") as pw_file:
                    #Reading old data
                    data = json.load(fp=pw_file)
            except FileNotFoundError:
                with open("passwords.json", "w") as pw_file:
                     json.dump(new_data,pw_file, indent=4)
            else:
                #updating old data with new data
                data.update(new_data)
                # print(data) #has type of dictionary
                with open("passwords.json","w") as pw_file:
                    #saving updated data
                    json.dump(data, pw_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator") 
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "bibekmanandhar2@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


generate_password_button = Button(text="Generate Password ", highlightthickness=0, command=generate_password)
generate_password_button.grid(row=3, column=2)



add_button = Button(text="Add",width=36, highlightthickness=0, command=add_password)
add_button.grid(row=4,column=1, columnspan=2)




window.mainloop()