# Task 2 — Firewall & System Hardening

## Host: 172.20.10.2
## Date: $(date)

## Steps performed
1. Installed and configured UFW (default deny incoming, allow outgoing).
2. Allowed SSH only (port 22).
3. Disabled unused services: avahi-daemon, cups, bluetooth.
4. Verified firewall status and captured logs.

## Evidence files
- ufw_status.txt
- systemctl_disabled_services.txt
- scans_listening_sockets.txt
- enabled_services.txt
- os_uname.txt
- os_release.txt

## Recommendations
- Keep system updated.
- Restrict unnecessary network services.
- Apply principle of least privilege.
