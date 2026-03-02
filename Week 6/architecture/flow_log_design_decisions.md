# Flow Log Design Decisions

## Subnet Selection Matrix

| Subnet | Enable | Sensitivity | Alert Tier |
|--------|--------|-------------|------------|
| Production-App | Yes | High | Tier 1 |
| Production-DB | Yes | Critical | Tier 1 |
| Dev | Yes | Medium | Tier 2 |
| Bastion | Yes | Critical | Tier 1 |
| Sandbox | No | Low | Tier 3 |

## Version Justification

v2 selected due to byte counters and Traffic Analytics integration.
v1 lacks sufficient telemetry for anomaly detection.

## Cost Model

Assumptions:
- 10 VMs
- 2GB/day per VM
- 20GB/day total
- 30-day hot retention

Scaling:

| VMs | GB/day |
|-----|--------|
| 10 | 20 |
| 50 | 100 |
| 100 | 200 |

## Retention Strategy

- 30 days hot (Log Analytics)
- 180 days cold (Storage)
