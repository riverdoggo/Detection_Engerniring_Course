# W4D4 — Severity & Alerting Strategy

## Objective
Define a consistent severity and alerting framework for control-plane detections.

## Design Principles
- High signal over high volume
- Actionable alerts only
- Clear escalation paths

## Severity Definitions
- Low: Informational, no response required
- Medium: Analyst review required
- High: Immediate investigation and escalation

## Alert Routing
- High: SOC escalation channels
- Medium: Standard analyst queue

## Alert Suppression
- Approved automation accounts
- Known change windows

## Outcome
Ensures detections translate into effective security operations.
