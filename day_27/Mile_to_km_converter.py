from tkinter import *

from Day_26.main import row

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=200, height=100)

# Entries
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
print(entry.get())
entry.grid(column=2, row=1, padx=10, pady=10)

# Label1
label1 = Label(text="is equal to")
# Adds some text to begin with.
label1.grid(column=1, row=2, padx=10, pady=10)

# Label2
label2 = Label(text="Miles")
# Adds some text to begin with.
label2.grid(column=3, row=1, padx=10, pady=10)

# Label3
label3 = Label(text="km")
# Adds some text to begin with.
label3.grid(column=3, row=2, padx=10, pady=10)

# Label4
label4 = Label(text="0")
# Adds some text to begin with.
label4.grid(column=2, row=2, padx=10, pady=10)

#Buttons
def action():
    user_input = int(entry.get())
    result = round(user_input * 0.621361, 4)
    label4.config(text=result)

# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=2, row=3, padx=10, pady=10)

mainloop()
