# Task 1 — Nmap System Vulnerability Assessment

## Network
- Subnet: 172.20.10.0/28
- Host: 172.20.10.2

## Commands
1. nmap -sn 172.20.10.0/28 -oN scans/hosts_discovery.txt
2. sudo nmap -sS -sV -p- 172.20.10.2 -oA scans/nmap_full_172.20.10.2
3. sudo nmap --script vuln 172.20.10.2 -oN scans/nmap_vuln_172.20.10.2.txt

## Summary
(Add open ports & vulnerabilities)

## Recommendations
- Close unused ports  
- Patch outdated services  
- Enable firewall rules  
