from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    # get search string
    string_to_check = website_entry.get()
    # open file and load json file
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        for key in data.keys():
            if string_to_check == key:
                messagebox.showinfo(string_to_check, "E-Mail: " + data[key]["email"] + "\nPassword: " + data[key]["password"])
                break
        else:
            messagebox.showinfo(string_to_check, "There is no password for this website in the database.")



def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for x in range(nr_letters)]
    password_list += [random.choice(symbols) for x in range(nr_symbols)]
    password_list += [random.choice(numbers) for x in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email": email_name,
            "password": password,
        }
    }

    if len(password) == 0 or len(website_name) == 0:
        messagebox.showerror("Something is wrong ...", "Either the website or your password is invalid.")
    else:
        try:
            with open("data.json", "r") as f:
                # Reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                # creating new json file and dumping new data
                json.dump(new_data, f, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)

            with open("data.json", "w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)
                print(data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Leks Password Manager")
window.config(bg="white", padx=50, pady=50)
# Canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
myImg = PhotoImage(file='logo.png')
canvas.create_image(0, 0, image=myImg, anchor='nw')
canvas.grid(row=0, column=1)

# Labels
website_label = Label(window, text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(window, text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(window, text="Password:", bg="white")
password_label.grid(row=3, column=0)

# Entryboxes
website_entry = Entry(width=24, bg="white")
website_entry.grid(row=1, column=1, sticky="w", padx=(10, 0))
website_entry.focus()

email_entry = Entry(width=43, bg="white")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=(10, 0))
email_entry.insert(0, "aflekler@gmail.com")

password_entry = Entry(width=24, bg="white")
password_entry.grid(row=3, column=1, sticky="w", padx=(10, 0))

# Frame for Buttons
# frame = Frame()
# frame.grid(row=3, column=2, sticky="W")
# Buttons
search_button = Button(width=14, text="search", command=find_password, bg="white")
search_button.grid(row=1, column=1, columnspan=2, stick="e")

generate_password_button = Button(width=14, text="Generate Password", command=generate_password, bg="white")
generate_password_button.grid(row=3, column=1, columnspan=2, sticky="e")

add_password_button = Button(width=36, text="Add", command=save_password, bg="white")
add_password_button.grid(row=4, column=1, columnspan=2, sticky="w", padx=(10, 0))

window.mainloop()
