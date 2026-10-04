from .banner import show_banner
from .menu import show_menu

def start():
    show_banner()

    while True:
        choice = show_menu()

        if choice == "1":
            print("\n[+] Encryption & Decryption selected.")

        elif choice == "2":
            print("\n[+] Network selected.")

        elif choice == "3":
            print("\n[+] Encoding & Decoding selected.")

        elif choice == "4":
            print("\n[+] Password selected.")

        elif choice == "5":
            print("\n[+] File Analysis selected.")

        elif choice == "6":
            print("\n[+] System selected.")

        elif choice == "7":
            print("\n[+] Utilities selected.")

        elif choice == "8":
            print("\n[+] About selected.")

        elif choice == "0":
            print("\n[*] Exiting Sinwar...")
            break

        else:
            print("\n[!] Invalid option.")