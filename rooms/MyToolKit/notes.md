# 🔧 Pentesting Tools

> 📌 **Overview:** These tools are widely used in cybersecurity for reconnaissance, scanning, exploitation, post-exploitation, and reporting.  
> They form the **"Swiss Army Knife"** of ethical hackers and red teamers.

---

## 🔍 Nmap

**Purpose:** Network discovery and port scanning tool.

**Use Cases:**

- Host discovery
- Service enumeration
- Detecting OS and versions

**Examples:**

- `nmap -sV target.com` → Detect services and versions
- `nmap -A target.com` → Aggressive scan (OS + version + scripts)

---

## 🔑 Hydra

**Purpose:** Password brute-forcing tool for network logins.

**Use Cases:**

- Cracking SSH, FTP, RDP, SMTP, HTTP logins
- Testing weak password policies

**Examples:**

- `hydra -l admin -P passwords.txt ssh://target.com`
- `hydra -L users.txt -P passlist.txt ftp://target.com`

---

## 📡 Wireshark

**Purpose:** Network packet capture and analysis tool.

**Use Cases:**

- Inspecting network traffic
- Detecting suspicious packets
- Debugging protocols

**Examples:**

- Capture HTTP traffic
- Filter: `http.request` or `ip.addr == 192.168.1.10`

---

## 💣 Metasploit

**Purpose:** Exploitation framework for vulnerabilities.

**Use Cases:**

- Exploiting known CVEs
- Post-exploitation (privilege escalation, pivoting)
- Generating payloads

**Examples:**

- `msfconsole` → Start Metasploit
- `search exploit windows` → Find exploits
- `use exploit/multi/handler` → Handle payloads

---

## 🌐 Burp Suite

**Purpose:** Web application security testing.

**Use Cases:**

- Intercepting and modifying HTTP/S requests
- Automated vulnerability scanning
- Testing for SQLi, XSS, CSRF

**Examples:**

- Proxy setup to capture traffic
- **Intruder** → brute-force login forms
- **Repeater** → test payloads manually

---

## 🛠️ SQLMap

**Purpose:** Automated SQL Injection testing tool.

**Use Cases:**

- Detecting SQL injection vulnerabilities
- Database dumping
- Gaining access to DB users

**Examples:**

- `sqlmap -u "http://target.com/id=1" --dbs`
- `sqlmap -u "http://target.com/id=1" --dump`

---

## 🔐 John the Ripper

**Purpose:** Password hash cracking tool.

**Use Cases:**

- Cracking system password files
- Testing password strength
- Supports multiple hash formats

**Examples:**

- `john --wordlist=rockyou.txt hashes.txt`
- `john --show hashes.txt`

---

## 📶 Aircrack-ng

**Purpose:** Wi-Fi network security testing.

**Use Cases:**

- Capturing WPA/WPA2 handshakes
- Cracking Wi-Fi passwords
- Monitoring wireless traffic

**Examples:**

- `airmon-ng start wlan0` → Enable monitor mode
- `aircrack-ng capture.cap -w wordlist.txt`

---

## 📂 Gobuster

**Purpose:** Directory and file brute-forcing on web servers.

**Use Cases:**

- Finding hidden directories
- Enumerating files, subdomains

**Examples:**

- `gobuster dir -u http://target.com -w wordlist.txt`
- `gobuster dns -d target.com -w subdomains.txt`

---

## 🌍 Nikto

**Purpose:** Web server vulnerability scanner.

**Use Cases:**

- Detecting outdated software
- Identifying common misconfigurations
- Scanning for dangerous files

**Examples:**

- `nikto -h http://target.com`

---

## 🖥️ Enum4linux

**Purpose:** SMB and Windows enumeration.

**Use Cases:**

- Extracting user lists
- Gathering system information
- Identifying SMB shares

**Examples:**

- `enum4linux -a target-ip`

---

## 🧑‍💻 Netcat (nc)

**Purpose:** “Swiss Army Knife” of networking.

**Use Cases:**

- Creating reverse shells
- Banner grabbing
- File transfers

**Examples:**

- `nc -lvp 4444` → Listen for connections
- `nc target.com 80` → Connect to a service

---

## 🔎 Recon-ng

**Purpose:** Reconnaissance and OSINT framework.

**Use Cases:**

- Domain info gathering
- Harvesting emails, subdomains
- Automated recon modules

**Examples:**

- `recon-ng` → Start console
- `marketplace install` → Add modules

---

## 🕵️‍♂️ TheHarvester

**Purpose:** Information gathering tool for emails, subdomains, hosts.

**Use Cases:**

- Collecting emails from public sources
- Finding subdomains via search engines
- Passive recon

**Examples:**

- `theHarvester -d target.com -b google`

---

## ⚔️ Social-Engineer Toolkit (SET)

**Purpose:** Social engineering attack framework.

**Use Cases:**

- Phishing campaigns
- Credential harvesting
- Payload generation

**Examples:**

- `setoolkit` → Start toolkit
- Clone website → Fake login page

---

## 🧩 Hashcat

**Purpose:** GPU-accelerated password cracking tool.

**Use Cases:**

- Brute-forcing hashes
- Mask attacks and rule-based cracking
- High-speed attacks with GPUs

**Examples:**

- `hashcat -m 0 hashes.txt wordlist.txt`

---

## 🚪 Netdiscover

**Purpose:** Network address discovery.

**Use Cases:**

- Detecting live hosts
- Mapping internal networks

**Examples:**

- `netdiscover -r 192.168.1.0/24`

---

## 📊 Maltego

**Purpose:** OSINT and data visualization tool.

**Use Cases:**

- Graph-based recon
- Linking people, domains, IPs
- Threat intelligence

**Examples:**

- Use **transforms** to connect data sources

---

## ⚡ Empire

**Purpose:** Post-exploitation and C2 framework.

**Use Cases:**

- Maintaining persistence
- Running PowerShell agents
- Lateral movement

**Examples:**

- `empire` → Start framework
- Generate stagers for Windows/Linux

---

## 🛡️ Nessus

**Purpose:** Vulnerability scanning and assessment tool.

**Use Cases:**

- Scanning networks, servers, and applications for known vulnerabilities
- Detecting misconfigurations and compliance issues
- Prioritizing risks with severity ratings (CVSS)

**Examples:**

- Run a scan against a subnet: `192.168.1.0/24`
- Generate detailed vulnerability reports (PDF/HTML)
- Use authenticated scans for deeper checks
