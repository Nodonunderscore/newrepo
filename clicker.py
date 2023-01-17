import tkinter as tk
win = tk.Tk()
win.title("basic clicker game")
win.geometry("290x300")
a = 0

def press():
    global a
    a += 1
    label.config(text=f"Times clicked: {a}")

label = tk.Label(master=win, text="Times clicked: none", width=150, height=20)
button = tk.Button(master=win, command=press, width=150, height=200)

label.pack()
button.pack()

win.mainloop()