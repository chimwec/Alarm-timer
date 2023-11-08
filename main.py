import tkinter as tk
import time

def start_timer():
    global start_time, running, paused, pause_time
    if not running and not paused:
        start_time = time.time() - pause_time if paused else time.time()  # Adjust start time if timer was paused
        running = True
        paused = False
        root.title("Timer is running")
        start_button.config(state=tk.DISABLED)  # Disable the "Start Timer" button
        pause_button.config(state=tk.NORMAL)   # Enable the "Pause Timer" button
    elif paused:
        start_time = time.time() - pause_time
        running = True
        paused = False
        root.title("Timer is running")
        start_button.config(state=tk.DISABLED)
        pause_button.config(state=tk.NORMAL)

def pause_timer():
    global pause_time, paused, running
    if running and not paused:
        pause_time = time.time() - start_time
        running = False
        paused = True
        root.title("Timer is paused")
        pause_button.config(state=tk.DISABLED)  # Disable the "Pause Timer" button
        start_button.config(state=tk.NORMAL)   # Enable the "Start Timer" button

def update_timer():
    global running
    if running:
        current_time = int(time.time() - start_time)
        hours = current_time // 3600  # Calculate the hours
        minutes = (current_time % 3600) // 60  # Calculate the minutes
        seconds = current_time % 60  # Calculate the remaining seconds
        timer_label.config(text=f"Elapsed Time: {hours} hours {minutes} minutes {seconds} seconds", font=("Arial", 24))
    root.after(1000, update_timer)

root = tk.Tk()
root.title("Timer")
root.configure(bg="lightblue")  # Set background color

start_button = tk.Button(root, text="Start Timer", command=start_timer, font=("Arial", 14))
start_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause Timer", command=pause_timer, font=("Arial", 14))
pause_button.pack(pady=10)
pause_button.config(state=tk.DISABLED)  # Initially disable the "Pause Timer" button

timer_label = tk.Label(root, text="Press 'Start Timer'", font=("Arial", 18))
timer_label.pack(pady=10)

start_time = None
running = False
pause_time = 0  # Variable to store time when paused
paused = False

if __name__ == "__main__":
    root.after(1000, update_timer)  
    root.mainloop()

