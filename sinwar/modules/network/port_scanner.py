import socket


def scan_port(target, port, timeout=0.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))

            return result == 0
    except socket.gaierror:
        return False


def run():
    print("\n=== Port Scanner ===")

    target = input("Enter IP or hostname: ")

    try:
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))

        if not (1 <= start_port <= end_port <= 65535):
            print("\n[!] Invalid port range.")
            return

    except ValueError:
        print("\n[!] Ports must be numbers.")
        return

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[!] Could not resolve target.")
        return

    print(f"\n[*] Scanning {target} ({target_ip})...")
    print(f"[*] Ports: {start_port}-{end_port}\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            open_ports.append(port)
            print(f"[+] Port {port} is OPEN")

    print("\n=== Scan Complete ===")

    if not open_ports:
        print("[-] No open ports found.")