import yaml
import tkinter as tk
from SerialPort import SerialPort
from Config import Config
from SerialTerminal import SerialTerminal
from CommandList import CommandList

class AtTool(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.serial = SerialPort(self)
        self.geometry('1000x1200+0+0')
        self.config = Config(self)
        self.pane = tk.PanedWindow(orient=tk.HORIZONTAL, sashwidth=5)
        self.pane.pack(fill=tk.BOTH, expand=1, padx=3, pady=3)
        self.serial_terminal = SerialTerminal(self.pane)
        self.command_list = CommandList(self.pane)
        self.pane.add(self.serial_terminal)
        self.pane.add(self.command_list)

if __name__ == '__main__':
    app = AtTool()
    app.mainloop()
