# W4D1 — Suspicious Role Assignments (IAM)

## Objective
Detect unauthorized or anomalous Azure RBAC role assignments that may indicate
privilege escalation or persistence establishment.

## Threat Rationale
Control-plane privilege escalation enables full subscription compromise.
Role assignment abuse is a primary technique used by cloud attackers post-access.

## Telemetry Source
AzureActivity (Administrative operations)

## Detection Focus
- Role assignment creation
- Assignment scope (resource group vs subscription)
- Role criticality

## High-Level Detection Logic
Monitor successful role assignment write operations and evaluate:
- Assigned role sensitivity
- Assignment scope
- Caller identity and origin

## Severity Model
- High: Owner, Contributor, or User Access Administrator at subscription scope
- Medium: Non-admin roles or limited scopes

## Analyst Considerations
- Validate business justification
- Confirm change approval
- Correlate with other control-plane events

## Outcome
Provides early warning of Azure privilege escalation attempts.
