from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
result = 2 * 3.445
print(result)
my_name ="Jalal"

def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    timer_label.config(text="Timer", font=(FONT_NAME, 24, 'bold'), bg=YELLOW, fg=GREEN)
    checkmark_label["text"] = ""
    reps = 0


# ---------------------------- TIMER PAUSE ------------------------------- #
def pause_timer():
    global timer
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    if reps == 8:
        counter(long_break_seconds)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        counter(work_seconds)
    else:
        timer_label.config(text="Short Break", fg=PINK)
        counter(short_break_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def counter(count):
    global reps
    global timer
    minutes = str(count//60)
    seconds = str(count % 60)
    if count % 60 < 10:
        seconds = "0" + str(count % 60)
    canvas.itemconfig(canvas_text, text=minutes + ":" + seconds)
    if count > 0:
        timer = window.after(1000, counter, count-1)
    elif count == 0 and reps % 2 == 1:
        checkmark_label["text"] = checkmark_label["text"] + "✔"
        start_timer()
    elif reps == 8:
        checkmark_label["text"] = checkmark_label["text"] + "\n"


window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)


timer_label = Label(text="Timer", font=(FONT_NAME, 24, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
picture = PhotoImage(file="tomato.png")
canvas.create_image(100, 102, image=picture)
canvas_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=("Arial", 12, 'normal'), command=start_timer)
start_button.grid(row=2, column=0)

pause_button = Button(text="pause", font=("Arial", 12, 'normal'), command=pause_timer)
pause_button.grid(row=2, column=1)

reset_button = Button(text="reset", font=("Arial", 12, 'normal'), command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(text="", font=(FONT_NAME, 24, 'bold'), bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)

window.mainloop()
