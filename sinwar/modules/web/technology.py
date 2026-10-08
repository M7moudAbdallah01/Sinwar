import re

import requests


TIMEOUT = 10


def _normalize_url(url):
    url = url.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url


def _detect_technologies(response):
    technologies = set()

    headers = {
        key.lower(): value.lower()
        for key, value in response.headers.items()
    }

    html = response.text.lower()

    # -----------------------------------------------------
    # Server
    # -----------------------------------------------------

    server = headers.get("server")

    if server:
        technologies.add(
            f"Server: {server}"
        )

    # -----------------------------------------------------
    # Powered By
    # -----------------------------------------------------

    powered_by = headers.get("x-powered-by")

    if powered_by:
        technologies.add(
            f"Powered By: {powered_by}"
        )

    # -----------------------------------------------------
    # WordPress
    # -----------------------------------------------------

    if (
        "wp-content/" in html
        or "wp-includes/" in html
        or "wordpress" in html
    ):
        technologies.add("WordPress")

    # -----------------------------------------------------
    # Laravel
    # -----------------------------------------------------

    if (
        "laravel_session" in headers.get(
            "set-cookie",
            ""
        )
        or "laravel" in html
    ):
        technologies.add("Laravel")

    # -----------------------------------------------------
    # React
    # -----------------------------------------------------

    if (
        "react" in html
        or "__next_data__" in html
    ):
        technologies.add("React / Next.js")

    # -----------------------------------------------------
    # Vue
    # -----------------------------------------------------

    if "vue" in html:
        technologies.add("Vue.js")

    # -----------------------------------------------------
    # Angular
    # -----------------------------------------------------

    if (
        "ng-version" in html
        or "angular" in html
    ):
        technologies.add("Angular")

    # -----------------------------------------------------
    # Bootstrap
    # -----------------------------------------------------

    if "bootstrap" in html:
        technologies.add("Bootstrap")

    # -----------------------------------------------------
    # jQuery
    # -----------------------------------------------------

    if (
        "jquery" in html
        or "jquery.min.js" in html
    ):
        technologies.add("jQuery")

    # -----------------------------------------------------
    # PHP
    # -----------------------------------------------------

    if (
        "php" in headers.get(
            "x-powered-by",
            ""
        )
        or ".php" in html
    ):
        technologies.add("PHP")

    # -----------------------------------------------------
    # Cloudflare
    # -----------------------------------------------------

    if (
        "cloudflare" in headers.get(
            "server",
            ""
        )
        or "cf-ray" in headers
    ):
        technologies.add("Cloudflare")

    # -----------------------------------------------------
    # Nginx
    # -----------------------------------------------------

    if "nginx" in headers.get(
        "server",
        ""
    ):
        technologies.add("Nginx")

    # -----------------------------------------------------
    # Apache
    # -----------------------------------------------------

    if "apache" in headers.get(
        "server",
        ""
    ):
        technologies.add("Apache")

    # -----------------------------------------------------
    # Generator Meta Tag
    # -----------------------------------------------------

    generator = re.search(
        r'<meta[^>]+name=["\']generator["\'][^>]+content=["\']([^"\']+)',
        response.text,
        re.IGNORECASE
    )

    if generator:

        technologies.add(
            f"Generator: {generator.group(1)}"
        )

    return sorted(technologies)


def run():
    print("\n" + "=" * 42)
    print("          TECHNOLOGY DETECTION")
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
            timeout=TIMEOUT,
            headers={
                "User-Agent": "SINWAR-WebScanner/1.0"
            },
            allow_redirects=True
        )

    except requests.RequestException as error:

        print(
            f"\n[!] Request failed: {error}"
        )

        return

    print(
        f"\n[+] Final URL: {response.url}"
    )

    print(
        f"[+] HTTP Status: "
        f"{response.status_code}"
    )

    technologies = _detect_technologies(
        response
    )

    print("\n" + "-" * 42)

    if not technologies:

        print(
            "[-] No obvious technologies detected."
        )

    else:

        print(
            "[+] Detected technologies:"
        )

        for technology in technologies:
            print(
                f"    • {technology}"
            )

    print("-" * 42)