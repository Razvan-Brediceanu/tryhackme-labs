#!/usr/bin/env python3
# pip install pymisp
import os, csv
from pymisp import ExpandedPyMISP, MISPEvent, MISPAttribute
misp = ExpandedPyMISP(os.getenv("MISP_URL"), os.getenv("MISP_KEY"), ssl=True)
ev = MISPEvent(); ev.info = "Imported IoCs"; ev.distribution = 0; ev.threat_level_id = 2; ev.analysis = 1
with open("enriched_iocs.csv") as f:
    for row in csv.DictReader(f):
        attr = MISPAttribute(); attr.type = row["type"]; attr.value = row["value"]; ev.add_attribute(**attr)
ev = misp.add_event(ev)
print(f"[+] Created MISP event: {ev['Event']['id']}")
