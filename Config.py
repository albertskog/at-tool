import tkinter as tk

class Config(tk.LabelFrame):

    background_color = "#fff"

    def __init__(self, parent):
        tk.LabelFrame.__init__(self,
                               parent,
                               text="Configuration",
                               background=self.background_color)
        self.pack(fill=tk.BOTH, padx=4, pady=2, ipadx=5, ipady=4)
        
        self.port_label = tk.Label(self,
                                   text="Port:")
        self.port_label.pack(side=tk.LEFT)

        self.ports = parent.serial.get_ports()
        self.port_selector = tk.Menubutton(self, width=30)
        self.port_selector.menu = tk.Menu(self.port_selector)
        self.port_selector.configure(menu=self.port_selector.menu)
        self.refresh_button_callback()
        self.port_selector.pack(side=tk.LEFT)

        refresh_button = tk.Button(self,
                                   text="Refresh",
                                   command=self.refresh_button_callback,
                                   background=self.background_color)
        refresh_button.pack(side=tk.LEFT)
        self.baudrate_label = tk.Label(self,
                                       text="Baudrate:")
        self.baudrate_label.pack(side=tk.LEFT)

        self.baudrates = (9600, 115200)
        self.baudrate = tk.StringVar()
        self.baudrate.set(self.baudrates[0])
        self.baudrate_selector = tk.OptionMenu(self,
                                               self.baudrate,
                                               *self.baudrates)
        self.baudrate_selector.pack(side=tk.LEFT)

        connect_button = tk.Button(self,
                           text="Connect",
                           command=self.connect_buffon_callback,
                           background=self.background_color)
        connect_button.pack(side=tk.LEFT)

        disconnect_button = tk.Button(self,
                           text="Disconnect",
                           command=self.disconnect_buffon_callback,
                           background=self.background_color)
        disconnect_button.pack(side=tk.LEFT)

    def refresh_button_callback(self):
        ports = self.master.serial.get_ports()
        self.port_selector.menu.delete(index1=0, index2=self.port_selector.menu.index(tk.END))
        self.port_selector.configure(text=ports[-1])
        for port in ports:
            self.port_selector.menu.add_command(label=port)


    def connect_buffon_callback(self):
        port = self.master.config.port_selector["text"]
        baudrate = self.master.config.baudrate.get()
        self.master.serial.connect_port(port, baudrate)

    def disconnect_buffon_callback(self):
        self.master.serial.disconnect_port()