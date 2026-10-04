from urllib.parse import quote, unquote

def encode_fun(text):
    return quote(text)

def decode_fun(text):
    return unquote(text)


def run():
    print("\n=== URL Encoding ===")
    print("[1] Encode")
    print("[2] Decode")
    print("[0] Back")

    choice = input("\nSelect an option: ")

    if choice == "1":
        text = input("Enter text: ")
        result = encode_fun(text)
        print(f"\nResult: {result}")

    elif choice == "2":
        text = input("Enter encoded URL text: ")
        result = decode_fun(text)
        print(f"\nResult: {result}")

    elif choice == "0":
        return

    else:
        print("\n[!] Invalid option.")