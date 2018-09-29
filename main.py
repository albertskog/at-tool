import yaml
import tkinter as tk
from Config import Config
from SerialTerminal import SerialTerminal
from CommandList import CommandList

class AtTool(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('1200x1600+0+0')
        self.config = Config(self)
        self.pane = tk.PanedWindow(orient="horizontal", sashwidth=5)
        self.pane.pack(fill="both", expand=1, padx=3, pady=3)
        self.serial_terminal = SerialTerminal(self)
        self.command_list = CommandList(self)
        self.pane.add(self.serial_terminal)
        self.pane.add(self.command_list)

if __name__ == '__main__':
    app = AtTool()
    app.mainloop()
