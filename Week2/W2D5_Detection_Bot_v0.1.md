# Detection Bot v0.1 – Spec

## Intent
Detect unauthorized privilege escalation.

## Data Sources
AzureActivity

## Logic
Alert on successful roleAssignments/write outside approved admins.

## False Positives
Legitimate automation, CI/CD pipelines.

## Triage Steps
1. Identify Caller
2. Validate justification
3. Check follow-on activity
4. Revoke role if malicious