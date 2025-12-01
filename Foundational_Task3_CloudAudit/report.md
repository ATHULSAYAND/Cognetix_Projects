# Foundational Task 3 — Cloud Security Audit (AWS)

## Account
Account ID: $(aws sts get-caller-identity --query Account --output text)

## Evidence files (all original)
- iam_users.json
- iam_policies.json
- iam_roles.json
- mfa_status.json
- s3_buckets.json
- s3_acl_audit.txt
- s3_policy_audit.txt
- s3_encryption_audit.txt
- security_groups.json
- open_ports_risk.txt
- access_analyzer_findings.json
- ta_results.json
- cloudtrail_trails.json
- cloudtrail_status.json
- config_recorders.json
- iam_account_summary.json
- findings_summary.txt
- corrective_actions.txt

## Conclusion
A live read-only audit was performed using AWS CLI. Findings and corrective actions are provided for remediation.
