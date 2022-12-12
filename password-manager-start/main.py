from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass

def add_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #

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

# Textbox
website_entry = Entry(width=43, bg="white")
website_entry.grid(row=1, column=1, columnspan=2, sticky="w", padx=(10, 0))

email_entry = Entry(width=43, bg="white")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=(10, 0))

password_entry = Entry(width=24, bg="white")
password_entry.grid(row=3, column=1, sticky="w", padx=(10, 0))

# Frame for Buttons
# frame = Frame()
# frame.grid(row=3, column=2, sticky="W")
# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, bg="white")
generate_password_button.grid(row=3, column=1, columnspan=2, sticky="e")

add_password_button = Button(width=36, text="Add", command=add_password, bg="white")
add_password_button.grid(row=4, column=1, columnspan=2, sticky="w", padx=(10, 0))

window.mainloop()
