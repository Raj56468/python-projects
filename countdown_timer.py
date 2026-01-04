import time 

def countdown_timer(seconds):
    if seconds < 0:
        raise ValueError("Seconds must be a non-negative integer.")

    while seconds:
        min, sec = divmod(seconds, 60)
        timer_display = f"{min:02}:{sec:02}"
        print(timer_display, end="\r")
        time.sleep(1)
        seconds -= 1
    print("00:00\nTime's up!")
    
seconds = int(input("Enter the countdown time in seconds: "))

countdown_timer(int(seconds))