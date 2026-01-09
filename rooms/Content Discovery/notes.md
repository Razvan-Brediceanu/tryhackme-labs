# 🔍 Content Discovery

## 📌 Overview

Content Discovery teaches techniques for finding hidden or unlinked content on a web server that may expose sensitive files, directories, or functionality.

## 🔑 Key Concepts

### What is Content Discovery?

The process of identifying hidden paths, files, or endpoints that are not directly accessible through a website’s navigation.

### Manual Discovery Techniques

- Reviewing robots.txt
- Inspecting page source
- Observing URL patterns
- Checking error messages

### Automated Discovery

Using wordlists and brute-force techniques to discover:

- Hidden directories
- Backup files
- Admin panels
- Configuration files

### Common Targets

- `/admin`
- `/backup`
- `/config`
- `/test`
- Old or deprecated files

### Security Risks

Hidden content may expose:

- Sensitive data
- Debug pages
- Weak authentication
- Vulnerable endpoints

## 🛡️ Defensive Perspective

Proper access controls, file permissions, and removing unused content reduces attack surface.

## ✅ Key Takeaway

Content discovery is a critical reconnaissance step that often leads to identifying exploitable attack paths.

📅 **Completed on:** 9/4/2025  
🎯 **Difficulty:** Easy ✅
