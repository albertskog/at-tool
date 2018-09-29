import yaml
import tkinter as tk

class CommandList(tk.LabelFrame):
    
    command_labels = []

    def __init__(self, parent):
        tk.LabelFrame.__init__(self,
                               parent,
                               text="Commands")
        self.pack()
        self.load_commands()

    def load_commands(self):
        try:
            commands = yaml.load(open('commands.yaml', 'r'))
        except yaml.YAMLError:
            print("Error in command file")

        for command in commands:
            self.add_command(command['command'])

    def add_command(self, command):
        frame = tk.Frame(self)
        button = tk.Button(frame,
                           text="Send",
                           command=lambda: self.master.master.serial.send_data(command))
        button.pack(side=tk.LEFT)
        label = tk.Label(frame,
                         text=command,
                         font=("Consolas", 16))
        label.pack(side=tk.LEFT, anchor=tk.W)
        frame.pack(anchor=tk.W)
        self.command_labels.append([button, label])
