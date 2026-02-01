# Week 2 Day 4 – KQL Detection Patterns

## Spike
Sudden increase in normally low-volume operations.

## New Value
Detect first-time-seen Caller, Role, or ResourceId.

## Sequence
Ordered events: Role assignment → NSG change → KV access.

## Rare Term
Operations rarely used in normal admin workflows.

**Key Insight**
Patterns beat static rules. Behavior defines compromise.