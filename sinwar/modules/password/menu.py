def show_password_menu():
    print("\n" + "=" * 42)
    print("          PASSWORD MANAGER")
    print("=" * 42)

    print("[1] Generate & Save Password")
    print("[2] View Saved Passwords")
    print("[3] Delete Password")
    print("[0] Back")

    print("=" * 42)

    return input("[>] Select an option: ").strip()