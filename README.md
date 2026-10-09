# SINWAR

> **Security Information & Network Web Assessment Toolkit**

SINWAR is a Python-based security toolkit designed for **learning, defensive security assessment, and authorized penetration testing**. It provides a simple interactive CLI that groups common security utilities into one place.

![SINWAR Running](/images/run.png)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-v1.0.0-success)

---

## 👨‍💻 Author

**Mahmoud Abdallah**

Cybersecurity Learner & Penetration Testing Enthusiast

* GitHub: [@M7moudAbdallah01](https://github.com/M7moudAbdallah01)
* Portfolio: [Mahmoud A. Sharaf](https://m7moudabdallah01.github.io/My-Portfolio/)

---

## ⚠️ Responsible Use

SINWAR is intended for systems you own or have explicit permission to test.

**Do not** use it against third-party systems, accounts, networks, or applications without authorization. You are responsible for complying with applicable laws and rules of engagement.

---

## Features

### 🔐 Crypto

* Encryption / decryption utilities
* Hashing utilities

### 🌐 Network

* Port scanning
* DNS lookup

### 🛡️ Web Security

* Directory discovery
* Security headers analysis
* `robots.txt` / `sitemap.xml` discovery
* Basic technology detection
* JavaScript endpoint discovery
* Benign input reflection checks

### 🔤 Encoding

* Base64 encode/decode
* URL encode/decode
* Hex encode/decode

### 🔑 Password Manager

* Secure random password generation
* Configurable length
* Uppercase / lowercase / numbers / symbols
* Save passwords locally
* View saved passwords
* Delete saved passwords

> **Note:** The current password manager stores entries in local JSON. It is suitable for learning and local testing, but it is **not a production-grade encrypted password vault**.

---

## Project Structure

```text
SINWAR/
├── sinwar/
│   ├── __main__.py
│   ├── cli.py
│   ├── banner.py
│   ├── about.py
│   ├── menu.py
│   └── modules/
│       ├── crypto/
│       ├── network/
│       ├── encoding/
│       ├── web/
│       └── password/
├── requirements.txt
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .gitignore
└── .venv/  # Created locally during installation; not committed to Git
```

Your exact tree may contain additional helper files depending on the current version.

---

# Installation

## Requirements

* Linux
* Python 3.9 or newer
* Git
* Internet connection for installing Python dependencies

Check Python:

```bash
python3 --version
```

Check Git:

```bash
git --version
```

## 1. Clone the repository

```bash
git clone https://github.com/M7moudAbdallah01/Sinwar.git
cd Sinwar
```

## 2. Install system requirements

On Kali Linux or Debian-based distributions:

```bash
sudo apt update
sudo apt install -y python3-venv
```

## 3. Create a virtual environment

```bash
python3 -m venv .venv
```

## 4. Install dependencies

```bash
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

The `requirements.txt` file should include all Python dependencies required by the toolkit, including `requests` and `cryptography` if they are used by your modules.

## 5. Test the application

Run SINWAR using its Python package entry point:

```bash
.venv/bin/python -m sinwar
```

The main interactive menu should appear if the installation completed successfully.

## 6. Register the `sinwar` command

You can configure a command for your current Linux user so that you can launch SINWAR from any directory.

Run the following commands **from the SINWAR project directory**:

```bash
mkdir -p ~/.local/bin

PROJECT_DIR="$(pwd)"

cat > ~/.local/bin/sinwar <<EOF
#!/usr/bin/env bash

PROJECT_DIR="$PROJECT_DIR"

cd "\$PROJECT_DIR" || exit 1

exec "\$PROJECT_DIR/.venv/bin/python" -m sinwar "\$@"
EOF

chmod +x ~/.local/bin/sinwar
```

This creates a launcher at `~/.local/bin/sinwar`. It changes to the project directory before starting the Python package, ensuring that Python can locate the `sinwar` package.

## 7. Ensure the launcher directory is in PATH

Check your current `PATH`:

```bash
echo "$PATH"
```

If `~/.local/bin` is already included, no additional configuration is required.

If you use Zsh and the directory is missing, add it to your shell configuration:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

If you use Bash instead, add the same export line to `~/.bashrc` and reload it:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## 8. Run SINWAR from anywhere

You can now launch the toolkit without activating the virtual environment or navigating to the project directory:

```bash
sinwar
```

For example:

```bash
cd /tmp
sinwar
```

To verify which launcher is being used:

```bash
command -v sinwar
```

Expected output:

```text
/home/YOUR_USERNAME/.local/bin/sinwar
```

**Important:** The launcher uses the project location where it was created. If you move the SINWAR directory, recreate the launcher using the new project location.

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

* `200` — OK
* `301/302/307/308` — Redirects
* `401` — Authentication required
* `403` — Forbidden

### Security Headers

Checks common defensive HTTP headers, including:

* Strict-Transport-Security
* Content-Security-Policy
* X-Content-Type-Options
* X-Frame-Options
* Referrer-Policy
* Permissions-Policy

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

> **Never commit real passwords, API keys, tokens, or other secrets to GitHub.**

---

# Development

Create the environment:

```bash
python3 -m venv .venv
```

Install dependencies:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

Run the application:

```bash
.venv/bin/python -m sinwar
```

Alternatively, if you have configured the launcher, run:

```bash
sinwar
```

Before committing:

```bash
git status
git diff
```

---

# Recommended Git Workflow

Review your changes before committing:

```bash
git status
git diff
```

Stage the README and image:

```bash
git add README.md run.png requirements.txt
git commit -m "Update README and add running screenshot"
git push origin main
```

Then create the GitHub release, if you are ready to publish it:

```text
v1.0.0
```

---

# Roadmap

Possible future improvements:

* [ ] Encrypted password storage
* [ ] Configuration file
* [ ] Better logging
* [ ] JSON/CSV report export
* [ ] Improved web fingerprinting
* [ ] More network utilities
* [ ] Automated tests
* [ ] CI workflow
* [ ] PyPI/package installation
* [ ] Cross-platform testing

---

# Contributing

Pull requests and improvements are welcome.

Please read `CONTRIBUTING.md` before submitting changes.

---

# License

SINWAR is released under the MIT License.

See `LICENSE` for details.

---

## About the Project

SINWAR is an independent security-learning project created by **Mahmoud Abdallah** to explore practical Python security tooling and authorized security assessment workflows.

If you find a bug or have an improvement, open an issue or submit a pull request.

---

**Made with Python by Mahmoud Abdallah**
