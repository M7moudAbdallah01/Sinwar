import requests


SECURITY_HEADERS = {
    "Strict-Transport-Security":
        "HSTS",

    "Content-Security-Policy":
        "Content Security Policy",

    "X-Content-Type-Options":
        "MIME Sniffing Protection",

    "X-Frame-Options":
        "Clickjacking Protection",

    "Referrer-Policy":
        "Referrer Policy",

    "Permissions-Policy":
        "Permissions Policy"
}


def _normalize_url(url):
    url = url.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url


def run():
    print("\n" + "=" * 42)
    print("           SECURITY HEADERS")
    print("=" * 42)

    target = input(
        "[?] Target URL: "
    ).strip()

    if not target:
        print("[!] Target cannot be empty.")
        return

    target = _normalize_url(target)

    try:
        response = requests.get(
            target,
            timeout=10,
            headers={
                "User-Agent": "SINWAR-WebScanner/1.0"
            },
            allow_redirects=True
        )

    except requests.RequestException as error:
        print(f"\n[!] Request failed: {error}")
        return

    print(
        f"\n[+] Final URL: {response.url}"
    )

    print(
        f"[+] HTTP Status: "
        f"{response.status_code}"
    )

    print("\n" + "-" * 42)

    present = 0

    for header, description in SECURITY_HEADERS.items():

        value = response.headers.get(header)

        if value:

            present += 1

            print(f"[+] {header}")
            print(f"    {description}")
            print(f"    Value: {value}")

        else:

            print(f"[-] {header}")
            print(f"    {description}")
            print("    Not present")

        print()

    print("-" * 42)

    print(
        f"[+] Security headers present: "
        f"{present}/{len(SECURITY_HEADERS)}"
    )