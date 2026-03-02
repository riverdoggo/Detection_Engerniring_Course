# NSG Flow Logs Architecture

## Architecture Flow

Data Plane:
VM / NIC
  ↓
Network Security Group
  ↓
NSG Flow Logs (v2)
  ↓
Storage Account

Ingestion Boundary:
Storage Account
  ↓
Traffic Analytics

Query Boundary:
Traffic Analytics
  ↓
Log Analytics Workspace
  ↓
Detection Queries (KQL)

## Control vs Data Plane

- Data Plane: Traffic flows governed by NSG rules.
- Control Plane: NSG configuration and diagnostics settings.
- Ingestion Boundary: Storage + Traffic Analytics processing.
- Query Boundary: Log Analytics workspace used for detection engineering.

## Flow Log Schema Elements

| Field | Detection Value |
|-------|-----------------|
| Source IP | Host attribution |
| Destination IP | External contact analysis |
| Source Port | Ephemeral behavior |
| Destination Port | Service targeting |
| Flow Direction | Inbound vs outbound |
| Flow Status | Recon detection |
| Bytes Sent | Exfil detection |
| Bytes Received | Beacon symmetry |
| Time Window | Rate analysis |

## Hard Limits

- No payload inspection
- No process visibility
- No user identity
- Aggregated windows
