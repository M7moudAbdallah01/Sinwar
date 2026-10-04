def encode_fun(text):
    return text.encode("utf-8").hex()


def decode_fun(text):
    return bytes.fromhex(text).decode("utf-8")



def run():
    print("\n=== Hex Encoding ===")
    print("[1] Encode")
    print("[2] Decode")
    print("[0] Back")

    choice = input("\nSelect an option: ")

    if choice == "1":
        text = input("Enter text: ")
        result = encode_fun(text)
        print(f"\nResult: {result}")

    elif choice == "2":
        text = input("Enter Hex: ")
        result = decode_fun(text)
        print(f"\nResult: {result}")

    elif choice == "0":
        return

    else:
        print("\n[!] Invalid option.")