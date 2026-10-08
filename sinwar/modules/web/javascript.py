import re
from urllib.parse import urljoin, urlparse

import requests


TIMEOUT = 10


URL_PATTERN = re.compile(
    r"""
    (?:
        https?://[^\s"'<>]+
        |
        /[A-Za-z0-9_./?=&:%${}\-]+
    )
    """,
    re.VERBOSE
)


def _normalize_url(url):
    url = url.strip()

    if not url.startswith(
        ("http://", "https://")
    ):
        url = "https://" + url

    return url


def _get_script_urls(page_url, html):

    pattern = re.compile(
        r'<script[^>]+src=["\']([^"\']+)',
        re.IGNORECASE
    )

    scripts = set()

    for src in pattern.findall(html):

        full_url = urljoin(
            page_url,
            src
        )

        parsed = urlparse(full_url)

        if parsed.scheme in (
            "http",
            "https"
        ):
            scripts.add(full_url)

    return sorted(scripts)


def _extract_endpoints(js_content):

    matches = URL_PATTERN.findall(
        js_content
    )

    endpoints = set()

    for match in matches:

        value = match.strip()

        # Ignore very long random strings.
        if len(value) > 300:
            continue

        # Ignore obvious file references.
        if value.lower().endswith(
            (
                ".png",
                ".jpg",
                ".jpeg",
                ".gif",
                ".svg",
                ".woff",
                ".woff2",
                ".ttf",
                ".css"
            )
        ):
            continue

        endpoints.add(value)

    return endpoints


def run():

    print("\n" + "=" * 42)
    print("       JAVASCRIPT ENDPOINT DISCOVERY")
    print("=" * 42)

    target = input(
        "[?] Target URL: "
    ).strip()

    if not target:
        print("[!] Target cannot be empty.")
        return

    target = _normalize_url(target)

    session = requests.Session()

    session.headers.update({
        "User-Agent": "SINWAR-WebScanner/1.0"
    })

    try:

        response = session.get(
            target,
            timeout=TIMEOUT,
            allow_redirects=True
        )

    except requests.RequestException as error:

        print(
            f"\n[!] Request failed: {error}"
        )

        return

    print(
        f"\n[+] Page: {response.url}"
    )

    script_urls = _get_script_urls(
        response.url,
        response.text
    )

    if not script_urls:

        print(
            "\n[-] No external JavaScript files found."
        )

        return

    print(
        f"\n[+] JavaScript files found: "
        f"{len(script_urls)}"
    )

    endpoints = set()

    for index, script_url in enumerate(
        script_urls,
        start=1
    ):

        print(
            f"\n[*] [{index}/{len(script_urls)}] "
            f"{script_url}"
        )

        try:

            js_response = session.get(
                script_url,
                timeout=TIMEOUT
            )

            if js_response.status_code != 200:
                print(
                    f"    [-] HTTP "
                    f"{js_response.status_code}"
                )
                continue

            found = _extract_endpoints(
                js_response.text
            )

            for endpoint in found:
                endpoints.add(endpoint)

            print(
                f"    [+] Found: "
                f"{len(found)} possible references"
            )

        except requests.RequestException:

            print(
                "    [-] Failed to download"
            )

    print("\n" + "=" * 42)
    print("             ENDPOINTS")
    print("=" * 42)

    if not endpoints:

        print(
            "[-] No obvious endpoints found."
        )

    else:

        for endpoint in sorted(endpoints):

            print(
                f"[+] {endpoint}"
            )

    print("\n[+] Discovery complete.")