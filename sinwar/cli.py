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
from .modules.network.menu import show_network_menu
from .modules.network.port_scanner import run as run_port_scanner
from .modules.network.dns_lookup import run as run_dns_lookup

from .modules.password.menu import show_password_menu
from .modules.password.manager import (
    run_generate_password,
    run_view_passwords,
    run_delete_password
)

from .about import show_about






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
            while True:
                network_choice = show_network_menu()

                if network_choice == "1":
                    run_port_scanner()
                elif network_choice == "2":
                    run_dns_lookup()
                elif network_choice == "0":
                    break
                else:
                    print("\n[!] Invalid option.")

        elif choice == "3":
            pass


        elif choice == "4":
            
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




        elif choice == "5":
            while True:

                password_choice = show_password_menu()

                if password_choice == "1":
                    run_generate_password()

                elif password_choice == "2":
                    run_view_passwords()

                elif password_choice == "3":
                    run_delete_password()

                elif password_choice == "0":
                    break

                else:
                    print("\n[!] Invalid option.")




        elif choice == "6":
            show_about()

        elif choice == "0":
            print("\n[*] Exiting Sinwar...")
            break

        else:
            print("\n[!] Invalid option.")