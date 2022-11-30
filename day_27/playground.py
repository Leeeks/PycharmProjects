# def add(*args):
#     summe = 0
#     for n in args:
#         summe += n
#     print(summe)
#
# add(1,2,3,4,5,6,7)

# label
from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100 , pady=100)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

button_1 = Button(text="click me", command=button_clicked)
button_1.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.grid(column=4, row=3)


mainloop()