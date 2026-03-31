import requests
import os
from dotenv import load_dotenv

load_dotenv()

VT_KEY = os.getenv("VT_API_KEY")
ABUSE_KEY = os.getenv("ABUSEIPDB_KEY")

def vt_lookup(ioc):
    headers = {"x-apikey": VT_KEY}
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ioc}" if "." in ioc else f"https://www.virustotal.com/api/v3/domains/{ioc}"
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            return data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        return None
    except:
        return None

def abuseipdb_lookup(ip):
    headers = {"Key": ABUSE_KEY, "Accept": "application/json"}
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}"
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            return {
                "abuseConfidenceScore": data.get("data", {}).get("abuseConfidenceScore", 0)
            }
        return None
    except:
        return None
