#!/usr/bin/env python3
import sys, subprocess, pathlib
rules = sys.argv[1]; target = sys.argv[2]
for p in pathlib.Path(target).rglob("*"):
    if p.is_file():
        subprocess.run(["yara", "-s", rules, str(p)], stdout=sys.stdout, stderr=sys.stderr)
