import yaml
import tkinter as tk

class TestApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('600x800+0+0')
        self.configure(background="red")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frame = tk.Frame(self)
        self.frame.configure(background="white")
        self.frame.grid(sticky="nsew")
        self.command_labels = []

    def add_command(self, text):
        frame = tk.Frame(self)
        button = tk.Button(frame,
                           text="Send")
        button.pack(side="left")
        label = tk.Label(frame,
                         text=text,
                         font=("Consolas", 16),
                         foreground="black")
        label.pack(side="left")
        frame.grid(sticky="nsew")
        self.command_labels.append([button, label])

    def run(self):
        self.mainloop()

t = TestApp()

try:
    commands = yaml.load(open('commands.yaml', 'r'))
except yaml.YAMLError:
    print("Error in command file")

for command in commands:
    print(command['command'])
    t.add_command(command['command'])

t.mainloop()