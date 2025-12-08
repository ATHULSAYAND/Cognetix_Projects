# Micro-segmentation Rules

Segments:
- Management
- App Frontend
- App Backend
- DB
- CI/CD
- Monitoring

Example DB rules:
DB-SG:
  Inbound:
    - From: App-Backend-SG, Ports: 5432 (Postgres), Protocol: TCP
    - From: Monitoring-SG, Ports: 9100 (metrics)
  Outbound:
    - To: Backup-SG, Ports: 443 (only for backups)
Notes: No inbound 0.0.0.0/0; all access via app proxies.
