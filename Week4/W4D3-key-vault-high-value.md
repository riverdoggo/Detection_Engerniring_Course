# W4D3 — Key Vault & High-Value Resource Protection

## Objective
Detect suspicious changes to Azure Key Vault and other Tier-0 resources.

## Threat Rationale
Key Vault compromise enables credential theft, ransomware deployment,
and long-term persistence across cloud environments.

## Telemetry Source
AzureActivity (Key Vault operations)

## Detection Focus
- Access policy modifications
- Vault configuration changes
- Vault deletion attempts

## Severity Model
- High: Access policy grants or vault deletion
- Medium: Non-destructive configuration changes

## Analyst Considerations
- Identify secrets or keys affected
- Validate requester identity
- Initiate credential rotation if required

## Outcome
Protects the most critical assets in the Azure control plane.
