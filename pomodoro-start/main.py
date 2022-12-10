from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
job_id = ""



# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global job_id
    global reps
    window.after_cancel(job_id)
    job_id = ""
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANIS M ------------------------------- #
def count_down(count):
    global job_id
    count_minutes = str(math.floor(count / 60)).zfill(2)
    count_seconds = str(count % 60).zfill(2)
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        job_id = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        checkmark_str = ""
        for i in range(0, math.floor((reps - 1) / 2)):
            checkmark_str += "✔"
        checkmark_label.config(text=checkmark_str)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
timer_label = Label(window, text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

checkmark_label = Label(window, font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=4, column=1)

# Buttons
start_button = Button(window, text="Start", command=start_timer, font=(FONT_NAME, 13, "bold"), fg=PINK, bg=YELLOW)
start_button.grid(row=3, column=0)

reset_button = Button(window, text="Reset", command=reset_timer, font=(FONT_NAME, 13, "bold"), fg=PINK, bg=YELLOW)
reset_button.grid(row=3, column=2)

# Canvas
canvas = Canvas(width=210, height=224)
canvas.config(bg=YELLOW, bd=0, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
