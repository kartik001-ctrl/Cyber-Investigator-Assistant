#!/usr/bin/env python3
import argparse, os
from rich.console import Console
from rich.table import Table
from core.extractor import extract_iocs
from core.hasher import sha256_text
from core.case import create_case, load_case, save_case
from core.timeline import log_event
from core.enrich import vt_lookup, abuseipdb_lookup

console = Console()

def analyze_text(text, case=None):
    iocs = extract_iocs(text)
    hash_val = sha256_text(text)

    console.print("\n[bold cyan]Extracted IOCs[/bold cyan]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Type")
    table.add_column("Value")
    table.add_column("Threat Info")

    for t, vals in iocs.items():
        for val in vals:
            threat = {}
            if t == "ip":
                threat = abuseipdb_lookup(val) or {}
            else:
                threat = vt_lookup(val) or {}
            table.add_row(t, val, str(threat))
    console.print(table)
    console.print(f"\n[bold green]Evidence SHA256[/bold green]: {hash_val}")

    if case:
        case["iocs"].update(iocs)
        log_event(case, f"Analyzed text with hash {hash_val}")

def main():
    parser = argparse.ArgumentParser(description="TraceFusion Advanced CLI")
    parser.add_argument("-t","--text", help="Analyze text")
    parser.add_argument("-f","--file", help="Analyze file")
    parser.add_argument("-c","--case", help="Case name")
    args = parser.parse_args()

    os.makedirs("cases", exist_ok=True)
    case = path = None

    if args.case:
        try:
            case, path = load_case(args.case)
            console.print(f"[bold green]+ Loaded case: {args.case}[/bold green]")
        except:
            case, path = create_case(args.case)
            console.print(f"[bold green]+ Created new case: {args.case}[/bold green]")

    if args.text:
        analyze_text(args.text, case)
    elif args.file:
        with open(args.file) as f:
            data = f.read()
        analyze_text(data, case)

    if case:
        save_case(case, path)
        console.print("[bold green]+ Case saved[/bold green]")

if __name__=="__main__":
    main()
