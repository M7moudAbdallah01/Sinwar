# SINWAR

> **Security Information & Network Web Assessment Toolkit**

SINWAR is a Python-based security toolkit designed for **learning, defensive security assessment, and authorized penetration testing**. It provides a simple interactive CLI that groups common security utilities into one place.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-v1.0.0-success)

## ⚠️ Responsible Use

SINWAR is intended for systems you own or have explicit permission to test.

Do **not** use it against third-party systems, accounts, networks, or applications without authorization. You are responsible for complying with applicable laws and rules of engagement.

---

## Features

### 🔐 Crypto
- Encryption / decryption utilities
- Hashing utilities

### 🌐 Network
- Port scanning
- DNS lookup

### 🛡️ Web Security
- Directory discovery
- Security headers analysis
- `robots.txt` / `sitemap.xml` discovery
- Basic technology detection
- JavaScript endpoint discovery
- Benign input reflection checks

### 🔤 Encoding
- Base64 encode/decode
- URL encode/decode
- Hex encode/decode

### 🔑 Password Manager
- Secure random password generation
- Configurable length
- Uppercase / lowercase / numbers / symbols
- Save passwords locally
- View saved passwords
- Delete saved passwords

> **Note:** The current password manager stores entries in local JSON. It is suitable for learning and local testing, but it is **not a production-grade encrypted password vault**.

---

## Project Structure

```text
SINWAR/
├── cli.py
├── requirements.txt
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .gitignore
└── modules/
    ├── __init__.py
    ├── banner.py
    ├── about.py
    ├── crypto/
    ├── network/
    ├── encoding/
    ├── web/
    │   ├── menu.py
    │   ├── directory.py
    │   ├── headers.py
    │   ├── robots.py
    │   ├── technology.py
    │   ├── javascript.py
    │   └── reflection.py
    └── password/
        ├── menu.py
        ├── generator.py
        └── manager.py
```

Your exact tree may contain additional helper files depending on the current version.

---

# Installation

## Requirements

- Linux
- Python 3.9 or newer
- Git
- Internet connection for installing Python dependencies

Check Python:

```bash
python3 --version
```

Check Git:

```bash
git --version
```

## 1. Clone the repository

Replace `YOUR_USERNAME` with your GitHub username:

```bash
git clone https://github.com/YOUR_USERNAME/SINWAR.git
cd SINWAR
```

## 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

You should now see something similar to:

```text
(.venv) user@linux:~/SINWAR$
```

## 3. Install dependencies

```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Run SINWAR

### Option A — if `cli.py` is the project entry point

```bash
python3 cli.py
```

### Option B — if your repository is packaged as a Python module

```bash
python3 -m sinwar
```

> Use **only the command that matches your repository structure**. If your current project does not contain a `sinwar/__main__.py`, use `python3 cli.py`.

---

# Quick Start

After launching the tool, you should see the main menu:

```text
[1] Crypto
[2] Network
[3] Web Security
[4] Encoding
[5] Password Manager
[6] About
[0] Exit
```

Choose an option by entering its number.

Example:

```text
[>] Select an option: 3
```

---

# Web Security

The web module is intended for authorized assessment of websites and web applications.

### Directory Discovery

Provide a target URL and a wordlist:

```text
[1] Directory Discovery
```

The scanner checks candidate paths and reports useful HTTP status codes such as:

- `200` — OK
- `301/302/307/308` — Redirects
- `401` — Authentication required
- `403` — Forbidden

### Security Headers

Checks common defensive HTTP headers, including:

- Strict-Transport-Security
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

### Robots / Sitemap

Checks:

```text
/robots.txt
/sitemap.xml
```

### Technology Detection

Performs basic fingerprinting using HTTP headers and page content.

### JavaScript Endpoint Discovery

Finds JavaScript files and extracts obvious URL/path references for manual review.

### Input Reflection Check

Uses a harmless unique marker to determine whether a supplied parameter is reflected in the response.

This is **not an exploit engine**. Findings should be manually reviewed.

---

# Password Manager

The password manager can:

1. Generate a random password
2. Save it with a name
3. View saved entries
4. Delete an entry

Example:

```text
[1] Generate & Save Password
[2] View Saved Passwords
[3] Delete Password
[0] Back
```

The local `passwords.json` file is intentionally excluded from Git through `.gitignore`.

**Never commit real passwords, API keys, tokens, or other secrets to GitHub.**

---

# Development

Create the environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run:

```bash
python3 cli.py
```

Before committing:

```bash
git status
git diff
```

---

# Recommended Git Workflow

```bash
git add .
git commit -m "Prepare v1.0.0 release"
git push origin main
```

Then create the GitHub release:

```text
v1.0.0
```

---

# Roadmap

Possible future improvements:

- [ ] Encrypted password storage
- [ ] Configuration file
- [ ] Better logging
- [ ] JSON/CSV report export
- [ ] Improved web fingerprinting
- [ ] More network utilities
- [ ] Automated tests
- [ ] CI workflow
- [ ] PyPI/package installation
- [ ] Cross-platform testing

---

# Contributing

Pull requests and improvements are welcome.

Please read `CONTRIBUTING.md` before submitting changes.

---

# License

SINWAR is released under the MIT License.

See `LICENSE` for details.

---

## Author

**SINWAR** is a security-learning project focused on practical Python security tooling.

If you find a bug or have an improvement, open an issue or submit a pull request.
