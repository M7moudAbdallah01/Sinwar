import html
from urllib.parse import (
    parse_qsl,
    urlencode,
    urlparse,
    urlunparse
)

import requests


TIMEOUT = 10


MARKER = "SINWAR_REFLECTION_TEST_7F3A"


def run():

    print("\n" + "=" * 42)
    print("          INPUT REFLECTION CHECK")
    print("=" * 42)

    target = input(
        "[?] URL with parameter: "
    ).strip()

    if not target:
        print("[!] URL cannot be empty.")
        return

    parsed = urlparse(target)

    if not parsed.scheme:
        print(
            "[!] URL must include "
            "http:// or https://"
        )
        return

    parameters = parse_qsl(
        parsed.query,
        keep_blank_values=True
    )

    if not parameters:

        print(
            "\n[!] No query parameters found."
        )

        print(
            "[*] Example:"
        )

        print(
            "    https://example.com/search?q=test"
        )

        return

    print("\n[+] Parameters found:")

    for index, (name, value) in enumerate(
        parameters,
        start=1
    ):

        print(
            f"[{index}] {name} = {value}"
        )

    print()

    try:

        choice = int(
            input(
                "[>] Select parameter: "
            ).strip()
        )

    except ValueError:

        print("[!] Invalid selection.")
        return

    if choice < 1 or choice > len(parameters):

        print("[!] Invalid selection.")
        return

    selected_name = parameters[
        choice - 1
    ][0]

    # Replace only the selected parameter.
    modified_parameters = []

    for name, value in parameters:

        if name == selected_name:

            modified_parameters.append(
                (
                    name,
                    MARKER
                )
            )

        else:

            modified_parameters.append(
                (
                    name,
                    value
                )
            )

    new_query = urlencode(
        modified_parameters
    )

    test_url = urlunparse(
        (
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            parsed.params,
            new_query,
            parsed.fragment
        )
    )

    print(
        f"\n[*] Testing parameter: "
        f"{selected_name}"
    )

    try:

        response = requests.get(
            test_url,
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

    body = response.text

    print(
        f"[+] HTTP Status: "
        f"{response.status_code}"
    )

    if MARKER not in body:

        print(
            "\n[-] Marker was not reflected "
            "in the response."
        )

        return

    print(
        "\n[+] Marker was reflected "
        "in the response."
    )

    # Check a few broad contexts.
    if MARKER in html.escape(body):

        print(
            "[+] Marker appears in escaped "
            "HTML/text content."
        )

    else:

        print(
            "[!] Marker appears without "
            "being HTML-escaped in the response."
        )

        print(
            "[!] Manual security review "
            "is recommended."
        )

    print(
        "\n[*] This is a reflection indicator, "
        "not an exploit test."
    )