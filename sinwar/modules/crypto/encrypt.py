from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_text(text, key):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(text.encode("utf-8"))
    return encrypted.decode("utf-8")


def run():
    print("\n=== Encryption ===")

    text = input("Enter text: ")

    key = generate_key()
    encrypted = encrypt_text(text, key)

    print(f"\nKey: {key.decode()}")
    print(f"Encrypted: {encrypted}")