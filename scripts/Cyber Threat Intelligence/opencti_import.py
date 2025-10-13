#!/usr/bin/env python3
# pip install pycti
import os, csv
from pycti import OpenCTIApiClient
api = OpenCTIApiClient(os.getenv("OPENCTI_URL"), os.getenv("OPENCTI_TOKEN"))
with open("enriched_iocs.csv") as f:
    for r in csv.DictReader(f):
        api.indicator.create(
            name=r["value"], pattern_type="stix",
            pattern=f"[domain-name:value = '{r['value']}']" if r["type"]=="domain" else None,
            description="Imported IOC", valid_from="2024-01-01T00:00:00Z",
        )
print("[+] Pushed indicators to OpenCTI")
