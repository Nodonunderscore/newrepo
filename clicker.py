import tkinter as tk
win = tk.Tk()
win.title("basic clicker game")
win.geometry("500x300")
a = 0

def press():
    global a
    a += 1
    label.config(text=f"Times clicked: {a}")

label = tk.Label(master=win, text="Times clicked: none", width=400, height=50)
button = tk.Button(master=win, command=press, width=400, height=50)

label.grid(row=0, column=0)
button.grid(row=1, column=0)

win.mainloop()