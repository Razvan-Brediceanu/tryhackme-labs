#!/usr/bin/env python3
import sys, requests
h=sys.argv[1]
r=requests.get(f"https://hashlookup.circl.lu/lookup/{h}", timeout=10)
print(r.json())
