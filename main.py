from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#f8a89d"
RED = "#f26849"
DARKRED = "#f1583f"
GREEN = "#379b46"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ----------------------------- #

reps = 1
checks = ""
timer = None


def reset_click():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="timer", fg=GREEN)
    checkmark.config(text="")
    global reps
    reps = 1
    global checks
    checks = ""


# ---------------------------- TIMER MECHANISM ------------------------- #


def start_click():
    global reps
    global checks
    if reps == 9:
        reset_click()
        timer_label.config(text="werk")
    if reps == 8:
        timer_label.config(text="brek", fg=DARKRED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="brek", fg=RED)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="werk", fg=GREEN)
        countdown(WORK_MIN * 60)
    if reps % 2 == 0:
        checks += "✔"
        checkmark.config(text=checks)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM --------------------- #


def countdown(count):
    global timer
    global reps
    if count > 0:
        min = math.floor(count / 60)
        sec = count % 60
        canvas.itemconfig(timer_text, text=f"{min:02d}:{sec:02d}")
        timer = window.after(1000, countdown, count - 1)
    else:
        start_click()


# ---------------------------- UI SETUP -------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(
    100, 132, text="00:00", fill="white", font=(FONT_NAME, 25, "bold")
)
canvas.grid(column=1, row=1)

timer_label = Label(
    text="timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"), pady=20
)
timer_label.grid(column=1, row=0)

start_button = Button(
    text="start",
    width=5,
    fg="white",
    bg=PINK,
    activebackground=GREEN,
    activeforeground="white",
    font=(FONT_NAME),
    borderwidth=0,
    command=start_click,
)
start_button.grid(column=0, row=2)

reset_button = Button(
    text="reset",
    width=5,
    fg="white",
    bg=PINK,
    activebackground=GREEN,
    activeforeground="white",
    font=(FONT_NAME),
    borderwidth=0,
    command=reset_click,
)
reset_button.grid(column=2, row=2)

checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark.grid(column=1, row=3)

window.mainloop()
