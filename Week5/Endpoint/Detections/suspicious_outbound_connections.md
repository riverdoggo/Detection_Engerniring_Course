# Suspicious Outbound Connections

## Risk Classification

### Should Never Connect
- powershell.exe
- cmd.exe
- rundll32.exe

### Sometimes Connect
- mshta.exe
- wscript.exe
- java.exe

## Baseline Strategy
Rare destinations are defined as domains seen by less than 2 hosts in 14 days.

## Correlation Logic
Link process creation from execution detections with network events within 5 minutes.

## Pseudo-KQL
SELECT * FROM network
JOIN processes ON pid
WHERE process_name='powershell.exe'
AND destination NOT IN baseline_list;
