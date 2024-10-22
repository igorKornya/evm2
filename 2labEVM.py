import time
from tkinter import *
from threading import Thread

def update_label(label):
    colors = ["red", "green", "blue", "yellow", "purple", "cyan", "orange", "pink"]
    for i in range(10):
        current_text = label.cget("text")
        new_text = f"{current_text}\nHello!" if current_text else "Hello!"
        label.config(text=new_text, fg=colors[i % len(colors)])
        label.update()
        time.sleep(1)

def start_thread(label):
    thread = Thread(target=update_label, args=(label,))
    thread.start()

window = Tk()
window.geometry("500x500")
window.title("Colorful Hello")

label = Label(window, text="", font=("Helvetica", 14), width=30, height=10)
label.pack(pady=20)

start_button = Button(window, text="Start", command=lambda: start_thread(label))
start_button.pack(pady=20)

window.mainloop()
