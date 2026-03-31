import re

IOC_PATTERNS = {
    "ip": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
    "domain": r"\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    "sha256": r"\b[a-fA-F0-9]{64}\b"
}

def extract_iocs(text):
    results = {}
    for key, pattern in IOC_PATTERNS.items():
        results[key] = list(set(re.findall(pattern, text)))
    return results
