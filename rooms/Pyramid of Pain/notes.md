🛑 Pyramid of Pain
📌 Overview

The Pyramid of Pain is a model that shows how difficult it is for attackers when defenders detect and block different types of Indicators of Compromise (IOCs).
The higher up the pyramid, the more pain it causes the adversary.

Pyramid Levels

1. Hash Values

Unique identifiers for files (e.g., SHA256).

✅ Easy for defenders to detect.

❌ Easy for attackers to change.

Example: recompiling the same malware produces a new hash.

2. IP Addresses

Identify attacker infrastructure.

❌ Can be rotated quickly with new servers or proxies.

Example: swap to another VPS or use a different proxy pool.

3. Domain Names

Used in phishing or C2 infrastructure.

⚠️ Harder to replace than IPs (due to registration, reputation, blacklists).

Example: burned domain requires new registration and warm-up.

4. Network / Host Artifacts

Examples: registry keys, C2 traffic patterns, malware behavior.

💀 More costly for attackers to modify.

Example: custom JA3/TLS fingerprint or specific registry path.

5. Tools

Software used by attackers (e.g., Cobalt Strike, Metasploit).

🔧 If defenders block these, attackers must rebuild or find new tools.

Example: EDR rules neuter Cobalt Strike beacons → attacker shifts to custom RAT.

6. TTPs (Tactics, Techniques, and Procedures)

Represent attacker plans and objectives.

🎯 Hardest to change — detection at this level disrupts entire campaigns.

Example: spotting attacker’s living-off-the-land lateral movement.

✅ Key Takeaway

The higher you go up the pyramid, the more disruptive detection is for the attacker.

Defenders should focus on TTPs and Tools, not only on hashes and IPs.

📅 Completed on: 9/2/2025
🎯 Difficulty: Easy ✅
