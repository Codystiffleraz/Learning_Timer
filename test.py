import random

mins = 600
max_times = 120
min_times = 200
print(max_times, round(min_times))

# Randint and sub tract from mins

if mins == 0:
    
while mins > 0:
    if mins < min_times:
        break
    r = random.randint(max_times, round(min_times))
    mins -= r
    
    countdown(r)

countdown():
    countdown 10