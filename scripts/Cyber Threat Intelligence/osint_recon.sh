#!/usr/bin/env bash
set -e
TARGET="$1"
echo "[*] WHOIS"
whois "$TARGET" | tee "whois_$TARGET.txt"
echo "[*] DNS"
dig +short A "$TARGET" | tee "dns_$TARGET.txt"
echo "[*] HTTP headers"
curl -I "http://$TARGET" -m 10 -sS | tee "headers_$TARGET.txt"
