import requests

def get_subdomains_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        if response.ok:
            data = response.json()
            subdomains = set()
            for entry in data:
                name_value = entry.get("name_value", "")
                for sub in name_value.split("\n"):
                    if domain in sub:
                        subdomains.add(sub.strip())
            return sorted(subdomains)
    except Exception as e:
        print(f"[!] Error querying crt.sh: {e}")
    return []

def get_subdomains_certspotter(domain):
    url = f"https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names"
    headers = {'User-Agent': 'Sublist3r-Python'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.ok:
            data = response.json()
            subdomains = set()
            for entry in data:
                for dns in entry.get("dns_names", []):
                    if domain in dns:
                        subdomains.add(dns)
            return sorted(subdomains)
    except Exception as e:
        print(f"[!] Error querying Cert Spotter: {e}")
    return []

def subdomain_enum(domain):
    print(f"\n[*] Enumerating subdomains for: {domain}\n")
    results = set()

    print("[+] Querying crt.sh...")
    results.update(get_subdomains_crtsh(domain))

    print("[+] Querying Cert Spotter...")
    results.update(get_subdomains_certspotter(domain))

    print(f"\n[+] Found {len(results)} unique subdomains:\n")
    for subdomain in sorted(results):
        print(subdomain)

if __name__ == "__main__":
    domain = input("Enter the domain (e.g., example.com): ").strip()
    if not domain or "." not in domain:
        print("[!] Invalid domain.")
    else:
        subdomain_enum(domain)
