#!/usr/bin/env python3
import os, csv
# TODO: add calls to services you’re allowed to use (respect TOS/rate limits)
# Example placeholder enrichment fields:
rows=[]
with open("artifacts_iocs.csv") as f:
    for t,v in csv.DictReader(f):
        rows.append({"type":t,"value":v,"first_seen":"","last_seen":"","tags":""})
with open("enriched_iocs.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print("[+] wrote enriched_iocs.csv")
