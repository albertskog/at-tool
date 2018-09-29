import yaml
import tkinter as tk
from CommandList import CommandList

class AtTool(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('600x800+0+0')
        self.configure(background="white")
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        self.frame = tk.Frame(self)
        self.frame.configure(background="green")
        # self.frame.grid(sticky="nsew")
        self.command_list = CommandList(self)

if __name__ == '__main__':
    app = AtTool()
    app.mainloop()
