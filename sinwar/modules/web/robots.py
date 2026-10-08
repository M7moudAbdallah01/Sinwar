import requests
from urllib.parse import urljoin


TIMEOUT = 10


def _normalize_url(url):
    url = url.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url.rstrip("/") + "/"


def _fetch(session, url):
    try:
        response = session.get(
            url,
            timeout=TIMEOUT,
            headers={
                "User-Agent": "SINWAR-WebScanner/1.0"
            },
            allow_redirects=True
        )

        return response

    except requests.RequestException:
        return None


def run():
    print("\n" + "=" * 42)
    print("          ROBOTS / SITEMAP")
    print("=" * 42)

    target = input(
        "[?] Target URL: "
    ).strip()

    if not target:
        print("[!] Target cannot be empty.")
        return

    base_url = _normalize_url(target)

    session = requests.Session()

    # =====================================================
    # robots.txt
    # =====================================================

    robots_url = urljoin(
        base_url,
        "robots.txt"
    )

    print(
        f"\n[*] Checking: {robots_url}"
    )

    robots_response = _fetch(
        session,
        robots_url
    )

    if robots_response is not None:

        print(
            f"[+] Status: "
            f"{robots_response.status_code}"
        )

        if robots_response.status_code == 200:

            print("\n========== robots.txt ==========\n")

            content = robots_response.text.strip()

            if content:
                print(content)
            else:
                print("[!] robots.txt is empty.")

        else:
            print(
                "[!] robots.txt was not available."
            )

    else:
        print(
            "[-] Could not connect to robots.txt."
        )

    # =====================================================
    # sitemap.xml
    # =====================================================

    sitemap_url = urljoin(
        base_url,
        "sitemap.xml"
    )

    print(
        f"\n[*] Checking: {sitemap_url}"
    )

    sitemap_response = _fetch(
        session,
        sitemap_url
    )

    if sitemap_response is not None:

        print(
            f"[+] Status: "
            f"{sitemap_response.status_code}"
        )

        if sitemap_response.status_code == 200:

            print("\n========== sitemap.xml ==========\n")

            content = sitemap_response.text.strip()

            if content:
                # Keep output manageable.
                if len(content) > 10000:
                    print(content[:10000])
                    print(
                        "\n[!] Output truncated."
                    )
                else:
                    print(content)

        else:
            print(
                "[!] sitemap.xml was not available."
            )

    else:
        print(
            "[-] Could not connect to sitemap.xml."
        )

    print("\n[+] Check complete.")