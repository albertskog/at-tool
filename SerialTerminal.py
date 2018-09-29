import tkinter as tk

class SerialTerminal(tk.LabelFrame):

    background_color = "#fff"

    def __init__(self, parent):
        tk.LabelFrame.__init__(self,
                               parent,
                               text="Serial port",
                               background=self.background_color)
        self.pack(fill=tk.BOTH, expand=1)

        self.terminal = tk.Listbox(self,
                                   width=50,
                                   font=("Consolas", 16))
        self.y_scroll = tk.Scrollbar(self.terminal,
                                     orient=tk.VERTICAL,
                                     command=self.terminal.yview)
        self.terminal.configure(yscrollcommand=self.y_scroll.set)
        self.terminal.pack(fill=tk.BOTH, expand=1, padx=2, pady=1)
        self.y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.frame = tk.Frame(self, background=self.background_color)
        self.frame.pack(fill=tk.X)

        self.send_button = tk.Button(self.frame,
                                     text="Send",
                                     command=self.send_callback)
        self.send_button.pack(side=tk.RIGHT)

        self.command_line = tk.Entry(self.frame)
        self.command_line.bind("<Return>", self.send_callback)
        self.command_line.pack(side=tk.LEFT, fill=tk.X, expand=1)

    def add_line(self, text):
        self.terminal.insert(tk.END, " " + text)
        self.terminal.yview_moveto(1)

    def send_callback(self, event=None):
        if self.master.serial.port.is_open:
            self.master.serial.send_data(self.command_line.get())
            self.command_line.delete(0, tk.END)
        else:
            self.add_line("Not connected")