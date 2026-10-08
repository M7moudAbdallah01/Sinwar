import concurrent.futures
from pathlib import Path
from urllib.parse import urljoin

import requests


DEFAULT_TIMEOUT = 5
MAX_WORKERS = 20


def _normalize_url(url):
    url = url.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url.rstrip("/") + "/"


def _load_wordlist(path):
    try:
        with open(
            path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            words = []

            for line in file:
                word = line.strip()

                if not word:
                    continue

                if word.startswith("#"):
                    continue

                words.append(word.lstrip("/"))

            return words

    except OSError:
        print("\n[!] Could not open wordlist.")
        return None


def _scan_path(session, base_url, path):
    target = urljoin(
        base_url,
        path
    )

    try:
        response = session.get(
            target,
            timeout=DEFAULT_TIMEOUT,
            allow_redirects=False
        )

        # Only report useful responses.
        if response.status_code in (
            200,
            201,
            202,
            204,
            301,
            302,
            307,
            308,
            401,
            403
        ):
            return {
                "url": target,
                "status": response.status_code,
                "length": len(response.content)
            }

    except requests.RequestException:
        pass

    return None


def run():
    print("\n" + "=" * 42)
    print("          DIRECTORY DISCOVERY")
    print("=" * 42)

    target = input(
        "[?] Target URL: "
    ).strip()

    if not target:
        print("[!] Target cannot be empty.")
        return

    wordlist_path = input(
        "[?] Wordlist path: "
    ).strip()

    if not wordlist_path:
        print("[!] Wordlist path cannot be empty.")
        return

    wordlist_path = Path(wordlist_path).expanduser()

    if not wordlist_path.exists():
        print("[!] Wordlist does not exist.")
        return

    if not wordlist_path.is_file():
        print("[!] Wordlist path is not a file.")
        return

    base_url = _normalize_url(target)

    words = _load_wordlist(wordlist_path)

    if words is None:
        return

    if not words:
        print("[!] Wordlist is empty.")
        return

    print(
        f"\n[*] Loaded {len(words)} paths."
    )

    print(
        f"[*] Target: {base_url}"
    )

    print(
        f"[*] Workers: {MAX_WORKERS}"
    )

    print("\n[*] Scanning...\n")

    session = requests.Session()

    session.headers.update({
        "User-Agent": "SINWAR-WebScanner/1.0"
    })

    results = []

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=MAX_WORKERS
    ) as executor:

        futures = [
            executor.submit(
                _scan_path,
                session,
                base_url,
                path
            )
            for path in words
        ]

        for future in concurrent.futures.as_completed(
            futures
        ):

            result = future.result()

            if result is not None:

                results.append(result)

                print(
                    f"[+] {result['status']} "
                    f"{result['url']} "
                    f"({result['length']} bytes)"
                )

    print("\n" + "=" * 42)
    print("             SCAN COMPLETE")
    print("=" * 42)

    print(
        f"[+] Interesting paths: "
        f"{len(results)}"
    )