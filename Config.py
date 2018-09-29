import tkinter as tk

class Config(tk.LabelFrame):

    background_color = "#fff"

    def __init__(self, parent):
        tk.LabelFrame.__init__(self,
                               parent,
                               text="Configuration",
                               background=self.background_color)
        self.pack(fill="both", padx=4, pady=2)
        
        self.port_label = tk.Label(self,
                                   text="Port:")
        self.port_label.pack(side="left")

        self.ports = ('train', 'plane', 'boat')
        self.port = tk.StringVar()
        self.port.set(self.ports[0])
        self.port_selector = tk.OptionMenu(self,
                                           self.port,
                                           *self.ports)
        self.port_selector.pack(side="left")
        button = tk.Button(self,
                           text="Refresh",
                           background=self.background_color)
        button.pack(side="left")

        self.baudrate_label = tk.Label(self,
                                       text="Baudrate:")
        self.baudrate_label.pack(side="left")

        self.baudrates = (9600, 115200)
        self.baudtate = tk.StringVar()
        self.baudtate.set(self.baudrates[0])
        self.baudrate_selector = tk.OptionMenu(self,
                                               self.baudtate,
                                               *self.baudrates)
        self.baudrate_selector.pack(side="left")

        button = tk.Button(self,
                           text="Connect",
                           background=self.background_color)
        button.pack(side="left")
        button = tk.Button(self,
                           text="Disconnect",
                           background=self.background_color)
        button.pack(side="left")

