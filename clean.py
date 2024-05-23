import os

def clear():
    # Untuk sistem operasi Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Untuk sistem operasi lain seperti macOS, Linux
    else:
        _ = os.system('clear')
