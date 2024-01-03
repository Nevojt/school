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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sek = WORK_MIN * 60
    short_break_sek = SHORT_BREAK_MIN * 60
    long_break_sek = LONG_BREAK_MIN * 60
    
    
    
    if reps % 8 == 0:
        count_down(long_break_sek)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sek)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sek)
        timer_label.config(text="Work", fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME,30, "bold"), fill="white")
canvas.grid(row=1, column=1, padx=10, pady=10)


timer_label = Label(window, text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1, padx=5, pady=10)


start_button = Button(window, text="Start", command=start_timer ,font=(FONT_NAME, 15, "bold"))
start_button.grid(row=2, column=0)

reset_button = Button(window, text="Reset", command=reset_timer, font=(FONT_NAME, 15, "bold"))
reset_button.grid(row=2, column=2)

check_marks = Label(window, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1, padx=5, pady=5)


window.mainloop()