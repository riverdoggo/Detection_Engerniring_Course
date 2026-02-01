# Week 2 Day 1 – Telemetry Architecture

## What Data Goes Where (Azure)

**Flow Overview**
1. Azure Resource (VM, NSG, Key Vault, Subscription)
2. Azure Diagnostic Settings
3. Azure Activity Log / Resource Logs
4. Data Collection Rules (DCR)
5. Log Analytics Workspace
6. KQL Queries / Sentinel / Detection Bot

**Mapped Tables**
| Source | Log Type | Log Analytics Table |
|------|--------|---------------------|
| Subscription | Activity Log | AzureActivity |
| NSG | Resource Logs | AzureDiagnostics |
| Key Vault | Audit Logs | AzureDiagnostics |
| RBAC | Administrative Events | AzureActivity |

**Security Truth**
Visibility is the baseline. If it isn’t logged centrally, it doesn’t exist operationally.