def show_web_menu():
    print("\n" + "=" * 42)
    print("            WEB SECURITY")
    print("=" * 42)

    print("[1] Directory Discovery")
    print("[2] Security Headers")
    print("[3] Robots.txt / Sitemap")
    print("[4] Technology Detection")
    print("[5] JavaScript Endpoint Discovery")
    print("[6] Input Reflection Check")
    print("[0] Back")

    print("=" * 42)

    return input("[>] Select an option: ").strip()