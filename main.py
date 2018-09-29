import yaml
import tkinter as tk
from SerialTerminal import SerialTerminal
from CommandList import CommandList

class AtTool(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('1200x1600+0+0')
        self.configure(background="red")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.serial_terminal = SerialTerminal(self)
        self.command_list = CommandList(self)

if __name__ == '__main__':
    app = AtTool()
    app.mainloop()
