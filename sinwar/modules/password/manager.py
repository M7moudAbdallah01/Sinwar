import json
from pathlib import Path

from .generator import generate_password


PASSWORD_FILE = Path(__file__).resolve().parent / "passwords.json"



def load_passwords():
    if not PASSWORD_FILE.exists():
        return []

    try:
        with open(
            PASSWORD_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, OSError):
        print("\n[!] Could not read password file.")
        return []



def save_passwords(passwords):
    try:
        with open(
            PASSWORD_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                passwords,
                file,
                indent=4,
                ensure_ascii=False
            )

        return True

    except OSError:
        print("\n[!] Could not save passwords.")
        return False



def run_generate_password():

    print("\n" + "=" * 42)
    print("       GENERATE & SAVE PASSWORD")
    print("=" * 42)

    password = generate_password()

    if password is None:
        return

    while True:

        name = input(
            "[?] What is this password for? "
        ).strip()

        if name:
            break

        print("[!] Please enter a name.")

    passwords = load_passwords()

    entry = {
        "name": name,
        "password": password
    }

    passwords.append(entry)

    # Save
    if save_passwords(passwords):

        print("\n[+] Password saved successfully.")

        print(f"[+] Name     : {name}")
        print(f"[+] Password : {password}")



def run_view_passwords():

    passwords = load_passwords()

    print("\n" + "=" * 50)
    print("             SAVED PASSWORDS")
    print("=" * 50)

    if not passwords:
        print("\n[!] No saved passwords.")
        return

    for index, entry in enumerate(
        passwords,
        start=1
    ):

        print(
            f"\n[{index}] "
            f"{entry.get('name', 'Unknown')}"
        )

        print(
            f"    Password: "
            f"{entry.get('password', '')}"
        )

    print("\n" + "=" * 50)



def run_delete_password():

    passwords = load_passwords()

    if not passwords:
        print("\n[!] No saved passwords.")
        return

    print("\n" + "=" * 42)
    print("             DELETE PASSWORD")
    print("=" * 42)

    for index, entry in enumerate(
        passwords,
        start=1
    ):

        print(
            f"[{index}] "
            f"{entry.get('name', 'Unknown')}"
        )

    print("[0] Cancel")

    try:
        choice = int(
            input("\n[>] Select password: ").strip()
        )

    except ValueError:
        print("[!] Invalid option.")
        return

    if choice == 0:
        return

    if choice < 1 or choice > len(passwords):
        print("[!] Invalid option.")
        return

    selected = passwords[choice - 1]

    print(
        f"\n[!] Selected: "
        f"{selected.get('name', 'Unknown')}"
    )

    confirm = input(
        "[?] Are you sure you want to delete it? [Y/N]: "
    ).strip().lower()

    if confirm != "y":
        print("[*] Delete cancelled.")
        return

    passwords.pop(choice - 1)

    if save_passwords(passwords):
        print("\n[+] Password deleted successfully.")