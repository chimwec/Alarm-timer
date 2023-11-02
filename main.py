import tkinter as tk
import time

def start_timer():
    global start_time, running
    start_time = time.time()  # Record the start time
    running = True
    root.title("Timer is running")
    start_button.config(state=tk.DISABLED) #Disables the "Start timer" button

def stop_timer():
    global running
    running = False
    root.title("Timer is stopped")
    start_button.config(state=tk.NORMAL)

def update_timer():
    if running:
        current_time = int(time.time() - start_time)
        hours = current_time // 3600    # Calculate the hours
        minutes = (current_time % 3600) // 60  # Calculate the minutes
        seconds = current_time % 60   # Calculate the remaining seconds
        timer_label.config(text=f"Elapsed Time: {hours} hours {minutes} minutes {seconds} seconds", font=("Arial", 24))
    root.after(1000, update_timer)
     

root = tk.Tk()
root.title("Timer")
root.configure(bg="lightblue")  # Set background color

start_button = tk.Button(root, text="Start Timer", command=start_timer, font=("Arial", 14))
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Timer", command=stop_timer, font=("Arial", 14))
stop_button.pack(pady=10)

timer_label = tk.Label(root, text="Press 'Start Timer'", font=("Arial", 18))
timer_label.pack(pady=10)

start_time = None
running = False

if __name__ == "__main__":
    root.after(1000, update_timer)  
    root.mainloop()
