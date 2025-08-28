import tldextract

def get_url_length(url: str) -> int:
    return len(url)

def has_ip_address(url: str) -> bool:
    import re
    return bool(re.search(r'(\d{1,3}\.){3}\d{1,3}', url))

def get_domain(url: str) -> str:
    extracted = tldextract.extract(url)
    return f"{extracted.domain}.{extracted.suffix}"

