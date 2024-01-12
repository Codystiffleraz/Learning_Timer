from tkinter import *
from tkinter import ttk
import math
import random
from playsound import playsound

minutes = 10
timer_ = None
MAX_TIMES = 120
MIN_TIMES = 200

def reset_timer():
    window.after_cancel(timer_)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text='Timer', fg='green')

def start_timer():
    seconds = minutes * 60
    if seconds == 0:
        canvas.itemconfig(timer_text, text="Finished")
    elif seconds < MIN_TIMES:
        timer_countdown(seconds)
        seconds = 0
    else:
        r = random.randint(MAX_TIMES, round(MIN_TIMES))
        seconds -= r
        timer_countdown(r)
    
    
def timer_countdown(count):
    
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds= f"0{count_seconds}"
    
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer_
        timer_ =  window.after(1000, timer_countdown, count - 1)
    else:
        start_timer()
    
    
window = Tk()

window.config(padx=100, pady=50, bg='green')

timer = Label(text='Timer', bg='black', fg='green', font=("Courier", 50))
timer.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg='black', highlightthickness=0)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 30, "bold"))
canvas.grid(column=2,row=2)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)




window.mainloop()




