#!/usr/bin/env python3 
import re, sys, csv, pathlib
text = pathlib.Path(sys.argv[1]).read_text(errors="ignore")

ips = set(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text))
domains = set(re.findall(r'\b[a-z0-9.-]+\.[a-z]{2,}\b', text, re.I))
urls = set(re.findall(r'https?://[^\s\'"]+', text, re.I))
hashes = set(re.findall(r'\b(?:[A-Fa-f0-9]{32}|[A-Fa-f0-9]{40}|[A-Fa-f0-9]{64})\b', text))

with open("artifacts_iocs.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["type","value"])
    for v in sorted(ips): w.writerow(["ipv4",v])
    for v in sorted(domains): w.writerow(["domain",v])
    for v in sorted(urls): w.writerow(["url",v])
    for v in sorted(hashes): w.writerow(["hash",v])
print("[+] wrote artifacts_iocs.csv")
