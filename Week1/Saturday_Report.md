# Investigation Report: The Rare Event

**Summary:** Detected an anomalous outlier in historical logs indicating a singular high-impact event.

**Query:**
StormEvents 
| summarize Count = count() by EventType 
| sort by Count asc 
| take 1

**Reasoning:** Rare events indicate tail-risk anomalies.

**Conclusion:** Rare event identified and logged.
