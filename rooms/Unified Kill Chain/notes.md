🛑 Unified Kill Chain

📌 Overview

The Unified Kill Chain (UKC) combines the Lockheed Martin Cyber Kill Chain and MITRE ATT&CK frameworks into a single model.
It gives defenders a more complete picture of attacker behavior across preparation, intrusion, and operation stages.

🔗 Stages of the Unified Kill Chain

1. Reconnaissance

Adversaries gather information about targets.

Examples: OSINT, scanning, social engineering.

2. Weaponization

Attackers craft malicious tools (e.g., malware, exploit payloads).

Example: building a phishing lure with a trojanized attachment.

3. Delivery

How the weapon reaches the victim.

Examples: phishing emails, malicious websites, USB drops.

4. Exploitation

Triggering the malicious code on the victim system.

Examples: exploiting vulnerabilities, tricking users into execution.

5. Installation

Establishing persistence on the victim’s machine.

Examples: registry modifications, scheduled tasks, implants.

6. Command and Control (C2)

Communication channel between attacker and compromised system.

Examples: HTTP(S) beacons, DNS tunneling, custom protocols.

7. Credential Access

Stealing authentication data to escalate privileges.

Tools: Mimikatz, keyloggers, credential dumping.

8. Lateral Movement

Moving through the network to reach valuable assets.

Techniques: pass-the-hash, remote services, RDP pivoting.

9. Privilege Escalation

Gaining higher-level access to systems.

Examples: exploiting misconfigurations, kernel exploits.

10. Discovery

Mapping the environment to identify targets.

Examples: network scans, AD enumeration, system queries.

11. Collection

Gathering sensitive data for exfiltration.

Examples: database dumps, file harvesting, screenshots.

12. Exfiltration

Removing stolen data from the victim’s environment.

Examples: cloud storage uploads, encrypted tunnels, email leaks.

13. Impact / Objectives

Final attacker goals (often destructive or disruptive).

Examples: ransomware encryption, data corruption, service shutdown.

✅ Key Takeaway

The Unified Kill Chain expands on the Cyber Kill Chain by aligning with ATT&CK TTPs.

It gives defenders visibility from initial recon all the way to impact, enabling stronger detection and defense strategies.

📅 Completed on: 9/4/2025
🎯 Difficulty: Medium ✅
