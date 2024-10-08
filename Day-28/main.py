import math
from tkinter import *

from matplotlib.pyplot import title
from numpy.ma.core import filled

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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    canvas.after_cancel(timer)
    canvas.itemconfig(timer_text_clock, text = "00:00")
    timer_text.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    # if it is  the 1st/3rd/5th/7th
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_text.config(text="Long Break", fg=RED)


    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_text.config(text="Break", fg=PINK)

    else:
        count_down(WORK_MIN * 60)
        timer_text.config(text="Work", fg=GREEN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text_clock, text=f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)



#EVENT DRIVEN


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(row=1,column=1)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text_clock = canvas.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME,35, "bold"))


timer_text =  Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_text.grid(row=0, column=1)

start_button =  Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button =  Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=3)

check_marks = Label(text="", bg=YELLOW)
check_marks.grid(column=1,row=2)

window.mainloop()