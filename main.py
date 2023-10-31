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
        timer_label.config(text=f"Elapsed Time: {current_time} seconds")
    root.after(1000, update_timer)  

root = tk.Tk()
root.title("Timer")

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

stop_button = tk.Button(root, text="Stop Timer", command=stop_timer)
stop_button.pack()

timer_label = tk.Label(root, text="Press 'Start Timer'")
timer_label.pack()

start_time = None
running = False

if __name__ == "__main__":
    root.after(1000, update_timer)  
    root.mainloop()
