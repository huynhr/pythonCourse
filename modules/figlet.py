import pyfiglet
from termcolor import colored

message = input('What is the message you want to send? ')
color = input('What color? ')

print(colored(pyfiglet.figlet_format(message), color))
