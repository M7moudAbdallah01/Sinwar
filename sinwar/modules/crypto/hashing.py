import hashlib


def hash_text(text, algorithm):
    hash_function = hashlib.new(algorithm)
    hash_function.update(text.encode("utf-8"))
    return hash_function.hexdigest()


def run():
    print("\n=== Hashing ===")
    print("[1] MD5")
    print("[2] SHA-1")
    print("[3] SHA-256")
    print("[4] SHA-512")
    print("[0] Back")

    choice = input("\nSelect a hash type: ")

    algorithms = {
        "1": "md5",
        "2": "sha1",
        "3": "sha256",
        "4": "sha512",
    }

    if choice == "0":
        return

    if choice not in algorithms:
        print("\n[!] Invalid option.")
        return

    text = input("Enter text: ")

    result = hash_text(text, algorithms[choice])

    print(f"\n{algorithms[choice].upper()}: {result}")