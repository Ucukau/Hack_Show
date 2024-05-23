import time 
from colorama import init, Fore, Back, Style

def icon_main():
    print(f'''
     {Fore.RED}
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@*#*#**#*@@@*@**"@*"@**"@*"@***@"$"@”"*@@@@@@@""#@"@
     @@@####@$$@""@@"@##*@*##@*##@@@@**@@*@@****@@@@@###
      @@@@@&_@$@&@__@&@{Fore.GREEN}_W_E_L_C_O_M_E_{Fore.RED}_@#-#$@&__@@@@@#
       @@@$@$#$@@@@$@@$$@$@@@@@@@@@@@@@@###_@_@_@_@@
{Style.RESET_ALL}
    ''')

def main_menu():
    print(f'''
    []———————————{Fore.GREEN}MENU{Style.RESET_ALL}————————————[]
    |{Fore.GREEN} ⟩ 1. Hack Screen{Fore.WHITE} {Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]        |
    |{Fore.RED} ⟩ 2. Error Screen{Fore.WHITE} {Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]       |
    |                             |
    | <—————————————————————————> |
    |                             |
    |{Fore.BLUE} ⟩ 3. Suport Admin{Fore.WHITE} {Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]       |
    |{Fore.BLUE} ⟩ 4. Donasi{Style.RESET_ALL} {Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]             |
    |{Fore.BLUE} ⟩ 5. Keluar{Style.RESET_ALL} {Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]             |
    ╔══════════════════════════════[]
    ║{Fore.YELLOW}Pilih Menu {Fore.WHITE}[{Fore.GREEN} 1, 2, 3, 4 {Style.RESET_ALL}]
    ║''')
