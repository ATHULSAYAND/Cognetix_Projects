# IAM Mappings

Persona: Dev (internal)
Resources: dev-api, dev-db
Access pattern: OAuth2 client credentials for services; user interactive via Azure AD SSO
Policy: Role 'dev-readonly' / 'dev-deploy' (least privilege); JIT for deploy
Enforcement: Azure AD group membership + Conditional Access + resource tag gating

Persona: Admin
Resources: management consoles, infra APIs
Access pattern: SSO with step-up MFA and JIT elevation
Policy: Breakglass accounts disabled except via ticketed JIT
Enforcement: Conditional Access, privileged identity management, session recording

Persona: CI/CD Service
Resources: build artifacts, deploy APIs
Access pattern: Role-assumed with permission boundaries
Policy: Narrow role with least privilege and short-lived credentials
Enforcement: AssumeRole with external ID and logging
