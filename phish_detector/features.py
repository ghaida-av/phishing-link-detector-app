# phish_detector/features.py
import re
import tldextract

def extract_features(url: str) -> dict:
    features = {}

    # Length of URL
    features["url_length"] = len(url)

    # Count of dots in URL
    features["dot_count"] = url.count(".")

    # Presence of an IP address
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    features["has_ip"] = 1 if re.search(ip_pattern, url) else 0

    # Length of domain
    ext = tldextract.extract(url)
    domain = ext.domain
    features["domain_length"] = len(domain)

    return features
