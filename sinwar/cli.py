from .banner import show_banner
from .menu import show_menu
from .modules.encoding.menu import show_encoding_menu
from .modules.encoding.base64_tool import run as run_base64
from .modules.encoding.url_tool import run as run_url
from .modules.encoding.hex_tool import run as run_hex
from .modules.crypto.menu import show_crypto_menu
from .modules.crypto.encrypt import run as run_encryption
from .modules.crypto.hashing import run as run_hashing
from .modules.crypto.decrypt import run as run_decryption









def start():
    show_banner()

    while True:
        choice = show_menu()

        if choice == "1":
            while True:
                crypto_choice = show_crypto_menu()

                if crypto_choice == "1":
                    run_encryption()
                elif crypto_choice == "2":
                    run_decryption()
                elif crypto_choice == "3":
                    run_hashing()
                elif crypto_choice == "0":
                    break
                else:
                    print("\n[!] Invalid option.")

        elif choice == "2":
            print("\n[+] Network selected.")

        elif choice == "3":
            
            while True:
                encoding_choice = show_encoding_menu()

                if encoding_choice == "1":
                    run_base64()

                elif encoding_choice == "2":
                    run_url()

                elif encoding_choice == "3":
                    run_hex()

                elif encoding_choice == "0":
                    break

                else:
                    print("\n[!] Invalid option.")

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