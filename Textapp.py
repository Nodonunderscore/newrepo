import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Text App')
        self.root.geometry('350x200')

        self.root.mainloop()
        return
    
if __name__ == '__main__':
    App()