import yaml

try:
    commands = yaml.load(open('commands.yaml', 'r'))
except yaml.YAMLError:
    print("Error in command file")

for command in commands:
    print(command['command'])