# W4D2 — NSG Exposure & Perimeter Changes

## Objective
Detect weakening or removal of Azure network security controls that expose workloads
to unauthorized network access.

## Threat Rationale
Perimeter reduction is a common preparatory step for lateral movement,
exploitation, or data exfiltration.

## Telemetry Source
AzureActivity (Network operations)

## Detection Focus
- NSG rule creation or modification
- NSG deletion events
- Public exposure indicators

## Severity Model
- Medium: Rule modifications increasing exposure
- High: NSG deletion or unrestricted inbound access

## Analyst Considerations
- Identify affected assets
- Determine exposure scope
- Validate against approved infrastructure changes

## Outcome
Detects silent or malicious reduction of cloud perimeter defenses.
