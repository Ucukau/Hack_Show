import menu
import clean
import time
import erMsg
from colorama import init, Fore, Back, Style
import os



while True:    
    menu.icon_main()
    menu.main_menu()
    print('''       
        ''')
    pilih = input(f"{Fore.BLACK}_   {Fore.WHITE}╚══⟩ ")
    if pilih == "":
        clean.clear()
        print("{Fore.RED}Pilihlah Sesuai Tampilan sekarang")
    elif pilih == "1":
        clean.clear()
        print ("untuk hack screen")              
    elif pilih == "2":    
        clean.clear()
        print ("untuk hack screen")              
    elif pilih == "3":
        clean.clear()
        print ("untuk hack screen")              
    elif pilih == "4":     
        clean.clear()
        print ("untuk hack screen")              
    elif pilih == "5":
        print(f"Program Dihentikan")
        break
    else:      
        clean.clear()
        menu.icon_main()
        menu.main_menu()
        print(f"{Fore.RED}Pilihan tidak valid. Silakan coba lagi.")
        erMsg.error()
