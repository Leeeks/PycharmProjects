from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(website_name) == 0:
        messagebox.showerror("Something is wrong ...", "Either the website or your password is invalid.")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered:\nEmail: {email_name}"
                                                           f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("myPasswords.txt", "a") as f:
                entry_string = f"{website_name} | {email_name} | {password}"
                f.write(f"{entry_string}\n")
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
website_entry = Entry(width=43, bg="white")
website_entry.grid(row=1, column=1, columnspan=2, sticky="w", padx=(10, 0))
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
generate_password_button = Button(text="Generate Password", command=generate_password, bg="white")
generate_password_button.grid(row=3, column=1, columnspan=2, sticky="e")

add_password_button = Button(width=36, text="Add", command=save_password, bg="white")
add_password_button.grid(row=4, column=1, columnspan=2, sticky="w", padx=(10, 0))

window.mainloop()
