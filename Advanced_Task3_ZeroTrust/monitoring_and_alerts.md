# Monitoring, Detection & Alerts

Identity risk KQL example:
event.dataset: "azure.auditlogs" and operationName: "Add member to role" and outcome: "success"

Elastic example:
{
  "query": {
    "bool": {
      "must": [
        { "match": { "event.action": "ssh.login_failed" } },
        { "range": { "@timestamp": { "gte": "now-24h" } } }
      ]
    }
  }
}
Suggested dashboards:
- Identity risk dashboard
- Network segmentation health
- Endpoint posture
- Top suspicious IPs/domains
