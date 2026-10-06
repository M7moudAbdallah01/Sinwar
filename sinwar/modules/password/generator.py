import secrets
import string


SYMBOLS = "!@#$%^&*()-_=+[]{}:,.?"


def generate_password():
    print("\n" + "=" * 42)
    print("          PASSWORD GENERATOR")
    print("=" * 42)

    while True:
        try:
            length = int(
                input("[?] Password length: ").strip()
            )

            if length < 4:
                print("[!] Password length must be at least 4.")
                continue

            if length > 256:
                print("[!] Password length cannot exceed 256.")
                continue

            break

        except ValueError:
            print("[!] Please enter a valid number.")

    print()

    # Character options
    use_upper = input(
        "[?] Include uppercase letters? [Y/N]: "
    ).strip().lower() == "y"

    use_lower = input(
        "[?] Include lowercase letters? [Y/N]: "
    ).strip().lower() == "y"

    use_numbers = input(
        "[?] Include numbers? [Y/N]: "
    ).strip().lower() == "y"

    use_symbols = input(
        "[?] Include symbols? [Y/N]: "
    ).strip().lower() == "y"

    character_sets = []

    if use_upper:
        character_sets.append(
            string.ascii_uppercase
        )

    if use_lower:
        character_sets.append(
            string.ascii_lowercase
        )

    if use_numbers:
        character_sets.append(
            string.digits
        )

    if use_symbols:
        character_sets.append(
            SYMBOLS
        )

    if not character_sets:
        print(
            "\n[!] You must select at least "
            "one character type."
        )
        return None

    if length < len(character_sets):
        print(
            f"\n[!] Password length must be at least "
            f"{len(character_sets)}."
        )
        return None

    password_chars = []

    for character_set in character_sets:
        password_chars.append(
            secrets.choice(character_set)
        )

    all_characters = "".join(character_sets)

    while len(password_chars) < length:
        password_chars.append(
            secrets.choice(all_characters)
        )

    secrets.SystemRandom().shuffle(
        password_chars
    )

    password = "".join(password_chars)

    print("\n[+] Generated Password:")
    print()
    print(password)
    print()

    return password