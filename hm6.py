import colorama

from colorama import init

from colorama import Fore, Back, Style

init(autoreset=True)

print(Fore.RED + 'Red text')
print(Fore.GREEN + 'Green text')
print(Fore.BLUE + 'Blue text')

print(Back.MAGENTA + 'Pink background')
print(Back.CYAN + 'Cyan background')
print(Back.YELLOW + 'Yellow background')

print(Style.BRIGHT + 'Bold text')
print(Style.DIM + 'Dim text')

print(Fore.BLUE + Back.MAGENTA + Style.BRIGHT + 'OMG!!!SO COLOURFUL:)')

print(Style.RESET_ALL)
print('Oh..the usual style again:(')
