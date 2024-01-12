"""
Add a beep to the end of the countdown 
    Maybe a 10 second sleep after
    Maybe a second countdown of 10 seconds
    Maybe bake in a 10 second countdown into the countdown
Add a 10-15 second countdown after the timer is up
    Have it subtract to the total time remaining
Add an input for minutes and have the program run on that
Fix UI and Layout
"""
mins = 10

def runoff(med=10, count):
    if count > 0:
        global timer_
        timer_ =  window.after(1000, timer_countdown, count - 1)