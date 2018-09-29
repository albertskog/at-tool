import tkinter as tk

class SerialTerminal(tk.LabelFrame):

    background_color = "#fff"

    def __init__(self, parent):
        tk.LabelFrame.__init__(self,
                               parent,
                               text="Serial port",
                               background=self.background_color)
        self.grid(row=0, column=0, sticky='NSEW')

        self.terminal = tk.Listbox(self)
        self.terminal.insert(tk.END, "asd")
        self.terminal.pack(fill="both", expand=1)

        self.frame = tk.Frame(self, background=self.background_color)
        self.frame.pack(fill="x")

        self.send_button = tk.Button(self.frame,
                                     text="Send")
        self.send_button.pack(side="right")

        self.command_line = tk.Entry(self.frame)
        self.command_line.pack(side="left", fill="x", expand=1)
