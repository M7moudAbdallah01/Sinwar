import socket


def run():
    print("\n=== DNS Lookup ===")

    domain = input("Enter domain: ").strip()

    if not domain:
        print("\n[!] Domain cannot be empty.")
        return

    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(domain)

        print(f"\nHostname: {hostname}")

        if aliases:
            print("\nAliases:")
            for alias in aliases:
                print(f"  - {alias}")

        print("\nIP Addresses:")
        for address in addresses:
            print(f"  - {address}")

    except socket.gaierror:
        print("\n[!] Could not resolve domain.")