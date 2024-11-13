# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_textbox.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def search_website_data():
    website = website_textbox.get().lower()
    if len(website) == 0:
        messagebox.showinfo(title="warning", message="the website field is empty.")
    else:
        try:
            with open("user_pass_database.json", "r") as my_file:
                my_data = json.load(my_file)
            username_email = my_data[website]["email"]
            password = my_data[website]["password"]
        except KeyError:
            messagebox.showinfo(title="warning", message="data not found!")
        except FileNotFoundError:
            messagebox.showinfo(title="warning", message="there is not data saved in the database.\n try adding"
                                                         "new data")
        else:
            messagebox.showinfo(title=website, message=f"username: {username_email}\npassword: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
file = open("user_pass_database.txt", "a")

def save_in_database():
    website_name = website_textbox.get().lower()
    email_user_name = email_username_textbox.get()
    password = password_textbox.get()
    new_data = {
        website_name: {
            "email": email_user_name,
            "password": password
                               }
    }

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="warning", message="Either the website or the password fields is empty.")
    elif messagebox.askokcancel(title="verification", message=f"the data you entered is:"
                                                              f" \nwebsite name: {website_name} "
                                                              f" \nemail/username: {email_user_name}"
                                                              f" \npassword: {password}\nis this data correct?"):
        try:
            with open("user_pass_database.json", "r") as my_file:
                my_data = json.load(my_file)
        except FileNotFoundError:
            my_data = new_data
        else:
            my_data.update(new_data)
        finally:
            with open("user_pass_database.json", "w") as my_file:
                json.dump(my_data, my_file, indent=4)

        website_textbox.delete(0, END)
        password_textbox.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
picture = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=picture)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Buttons
search_button = Button(text="Search", width=14, command=search_website_data)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=38,command=save_in_database)
add_button.grid(row=4, column=1, columnspan=2, sticky='E')

# Text Entries
website_textbox = Entry(width=26)
website_textbox.focus()
website_textbox.grid(row=1, column=1, sticky='E')

email_username_textbox = Entry(width=45)
email_username_textbox.insert(0, "s.jalalabasi94@gmail.com")
email_username_textbox.grid(row=2, column=1, columnspan=2, sticky='E')

password_textbox = Entry(width=26)
password_textbox.grid(row=3, column=1, sticky='E')

window.mainloop()

