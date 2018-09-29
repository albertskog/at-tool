import yaml
import tkinter as tk

class CommandList(tk.LabelFrame):
    
    background_color = "#fff"
    command_labels = []

    def __init__(self, parent):
        tk.LabelFrame.__init__(self,
                               parent,
                               text="Commands",
                               background=self.background_color)
        self.pack(fill="both", expand=1)
        self.load_commands()

    def load_commands(self):
        try:
            commands = yaml.load(open('commands.yaml', 'r'))
        except yaml.YAMLError:
            print("Error in command file")

        for command in commands:
            self.add_command(command['command'])

    def add_command(self, text):
        frame = tk.Frame(self, background=self.background_color)
        button = tk.Button(frame,
                           text="Send",
                           background=self.background_color)
        button.pack(side="left")
        label = tk.Label(frame,
                         text=text,
                         font=("Consolas", 16),
                         foreground="black",
                         background=self.background_color)
        label.pack(side="left", anchor="w")
        frame.pack(anchor="w")
        self.command_labels.append([button, label])