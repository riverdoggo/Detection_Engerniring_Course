# Sentinel Rule Analysis

## Rule 1: Suspicious PowerShell Download

Data Source: Sysmon Process Events

Detection Logic:
Detects PowerShell commands containing web download functions.

Severity: Medium

What to copy:
Efficient filtering and clear MITRE mapping.

What to avoid:
Overly broad command matching.

Improvement:
Add parent process conditions.

---

## Rule 2: Azure VM Suspicious Outbound

Data Source: AzureNetworkAnalytics

Detection Logic:
Detects unusual outbound traffic spikes.

Severity: Medium

What to copy:
Baseline comparison.

What to avoid:
Queries scanning entire dataset.

Improvement:
Add destination reputation checks.

---

## Rule 3: Credential Dumping Indicators

Data Source: SecurityEvent

Detection Logic:
Detects LSASS access attempts.

Severity: High

Improvement:
Correlate with process ancestry.

---

## Rule 4: Rare Process Execution

Data Source: Endpoint telemetry

Logic:
Detects processes rarely seen in environment.

Improvement:
Add threshold tuning.

---

## Rule 5: Suspicious Scheduled Task

Data Source: Windows logs

Logic:
Detects unusual scheduled task creation.

Improvement:
Include command-line validation.