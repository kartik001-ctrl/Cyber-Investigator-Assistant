# 🔍 TraceFusion CLI

TraceFusion is a Kali Linux-based OSINT & Threat Intelligence CLI tool designed to help analysts quickly extract, analyze, and enrich Indicators of Compromise (IOCs).

---

## 🚀 Features

- 🔍 Extract IOCs (IP, domain, SHA256)
- 🧠 Threat intelligence enrichment (VirusTotal + AbuseIPDB)
- 📂 Case management system
- 🕒 Timeline logging
- 🔐 Evidence hashing (SHA256)
- 🎨 Rich CLI output (tables, colors)

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/tracefusion-cli.git
cd tracefusion-cli
pip install -r requirements.txt

## Create .env file

VT_API_KEY=your_virustotal_api_key
ABUSEIPDB_KEY=your_abuseipdb_api_key

## Analyze text 
python3 tracefusion.py -t "IP 185.220.101.3 domain login-secure-update.com" -c test_case


## Analyze file
python3 tracefusion.py -f test_iocs.txt -c file_case

##📁 Output

Extracted IOCs

Threat intelligence data

Evidence SHA256 hash

Case file saved in /cases/


## Author
TeamredX
