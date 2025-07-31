# 🔍 Subdomain Enumerator

A simple Python tool to enumerate subdomains for a given domain using public certificate transparency logs from [crt.sh](https://crt.sh) and [Cert Spotter](https://certspotter.com).

## 📦 Features

- 🔎 Queries **crt.sh** and **Cert Spotter**.
- ✅ Returns deduplicated subdomains.
- 🚀 No API key required.
- 🐍 Pythonic and lightweight.

---

## 🛠 Requirements

- Python 3.6+
- `requests` module

Install the required dependency:

pip install requests


git clone https://github.com/your-username/subdomain-enumerator.git
cd subdomain-enumerator

python subdomain_enum.py

## [*] Enumerating subdomains for: example.com

[+] Querying crt.sh...
[+] Querying Cert Spotter...

[+] Found 8 unique subdomains:

api.example.com
dev.example.com
mail.example.com
test.example.com
www.example.com
...
