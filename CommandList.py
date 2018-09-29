import yaml
import tkinter as tk

class CommandList(tk.LabelFrame):
    
    command_labels = []

    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="Commands")

        try:
            commands = yaml.load(open('commands.yaml', 'r'))
        except yaml.YAMLError:
            print("Error in command file")

        for command in commands:
            print(command['command'])
            self.add_command(command['command'])
        
        self.pack()
    
    def add_command(self, text):
        frame = tk.Frame(self)
        button = tk.Button(frame, text="Send")
        button.pack(side="left")
        label = tk.Label(frame,
                         text=text,
                         font=("Consolas", 16),
                         foreground="black")
        label.pack(side="left")
        frame.grid(sticky="nsew")
        self.command_labels.append([button, label])