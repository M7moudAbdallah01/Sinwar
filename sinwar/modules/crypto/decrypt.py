from cryptography.fernet import Fernet


def decrypt_text(encrypted_text, key):
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_text.encode("utf-8"))
    return decrypted.decode("utf-8")


def run():
    print("\n=== Decryption ===")

    key = input("Enter key: ")
    encrypted_text = input("Enter encrypted text: ")

    try:
        decrypted = decrypt_text(encrypted_text, key.encode("utf-8"))
        print(f"\nDecrypted: {decrypted}")
    except Exception:
        print("\n[!] Decryption failed. Check the key and encrypted text.")