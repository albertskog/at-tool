import tkinter as tk

class SerialTerminal(tk.LabelFrame):

    def __init__(self, parent):
        tk.LabelFrame.__init__(self,
                               parent,
                               text="Serial port")
        self.pack(fill=tk.BOTH, expand=1)
        
        self.frame = tk.Frame(self)
        self.frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.terminal = tk.Text(self,
                                   width=50,
                                   font=("Consolas", 16))
        self.setup_tags()

        self.y_scroll = tk.Scrollbar(self,
                                     orient=tk.VERTICAL,
                                     command=self.terminal.yview)
        
        self.terminal.configure(yscrollcommand=self.y_scroll.set)

        self.y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.terminal.pack(fill=tk.BOTH, expand=1, padx=2, pady=1)


        self.send_button = tk.Button(self.frame,
                                     text="Send",
                                     command=self.send_callback)
        self.send_button.pack(side=tk.RIGHT)

        self.command_line = tk.Entry(self.frame)
        self.command_line.bind("<Return>", self.send_callback)
        self.command_line.pack(side=tk.LEFT, fill=tk.X, expand=1)

    def setup_tags(self):
        self.terminal.tag_config("error",
                                 background="#faa",
                                 lmargin1=3,
                                 spacing1=3,
                                 spacing3=3)
        self.terminal.tag_config("info",
                                 background="#eef",
                                 lmargin1=3,
                                 spacing1=3,
                                 spacing3=3)
        self.terminal.tag_config("command",
                                 lmargin1=3,
                                 spacing1=8,
                                 spacing3=2)
        self.terminal.tag_config("response",
                                 lmargin1=8,
                                 spacing1=1,
                                 spacing3=1)

    def add_line(self, text, tag="info"):
        self.terminal.insert(tk.END, "{}\n".format(text), tag)
        self.terminal.yview_moveto(1)

    def send_callback(self, event=None):
        if self.master.master.serial.port.is_open:
            self.master.master.serial.send_data(self.command_line.get())
            self.command_line.delete(0, tk.END)
        else:
            self.add_line("Not connected", "error")