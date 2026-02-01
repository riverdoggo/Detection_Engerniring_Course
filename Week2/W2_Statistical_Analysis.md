# Week 2 – Statistical Analysis

## Baseline (7 days)
```kql
AzureActivity
| summarize count() by bin(TimeGenerated, 1d)
```

## Anomaly Detection
```kql
AzureActivity
| summarize count() by bin(TimeGenerated, 1h)
| where count_ > 3 * avg(count_)
```

Screenshots: TODO (attach Sentinel graphs)