from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
FONT = "Arial"


# ---------------------------- SEARCH SITES ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"File not found")
    else:
        try:
            new_data = {key:value for key, value in data.items() if website in data}

            email = new_data[website]["email"]
            password = new_data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        except KeyError:
            messagebox.showerror(title="Error", message=f"Website {website} not found")
 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven`t left any fields empty")
    else:
        try:  
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                # Saving new data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)


# Label
website_label = Label(window, text="Website:", font=(FONT, 12))
website_label.grid(row=2, column=0)

user_name_label = Label(window, text="Email/Username:", font=(FONT, 12))
user_name_label.grid(row=3, column=0)

password_label = Label(window, text="Password:", font=(FONT, 12))
password_label.grid(row=4, column=0)

# Entry
website_entry = Entry(window, width=33)
website_entry.grid(row=2, column=1)
website_entry.focus()

email_entry = Entry(window, width=54)
email_entry.grid(row=3, column=1, columnspan=2)
email_entry.insert(0, "you`s@emai.com")

password_entry = Entry(window, width=33)
password_entry.grid(row=4, column=1)

# Buttons
gen_pass_button = Button(window, text="Generate Password", font=(FONT, 10), command=generate_password)
gen_pass_button.grid(row=4, column=2)

button_add = Button(window, text="Add", font=(FONT, 12), command=save)
button_add.grid(row=5, column=1, columnspan=2, sticky=W+E)

search_button = Button(window, text="Search", font=(FONT, 10), command=find_password)
search_button.grid(row=2, column=2, columnspan=2, sticky=W+E)


window.mainloop()