import json
import pandas as pd
import plotly.express as px

# -----------------------------
# Load Threat Feeds
# -----------------------------
with open("otx_feed.json") as f:
    otx = json.load(f)

with open("misp_feed.json") as f:
    misp = json.load(f)

abuse = open("abuseipdb_ips.txt").read().splitlines()

# -----------------------------
# Extract OTX Indicators
# -----------------------------
otx_iocs = []
for pulse in otx.get("pulses", []):
    for ind in pulse.get("indicators", []):
        otx_iocs.append({
            "source": "OTX",
            "type": ind.get("type"),
            "value": ind.get("indicator")
        })

# -----------------------------
# Extract MISP Indicators
# -----------------------------
misp_iocs = []
for attr in misp["Event"]["Attribute"]:
    misp_iocs.append({
        "source": "MISP",
        "type": attr["type"],
        "value": attr["value"]
    })

# -----------------------------
# Prepare AbuseIPDB Indicators
# -----------------------------
abuse_iocs = [{"source": "AbuseIPDB", "type": "ip", "value": ip} for ip in abuse]

# -----------------------------
# Merge all IOCs
# -----------------------------
df = pd.DataFrame(otx_iocs + misp_iocs + abuse_iocs)

df.to_csv("combined_iocs.csv", index=False)

# -----------------------------
# Frequency Visualization
# -----------------------------
count_df = df.groupby("source").size().reset_index(name="count")
fig = px.bar(count_df, x="source", y="count", title="Threat Feed IOC Distribution")
fig.write_html("threat_dashboard.html")
