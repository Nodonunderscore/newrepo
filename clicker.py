import tkinter as tk
win = tk.Tk()
win.title("basic clicker game")
a = 0

def press():
    a += 1
    label.config(text=f"Times clicked: {a}")

label = tk.Label(master=win, text="Times clicked: none")
button = tk.Button(master=win, command=press)

win.mainloop()