# Persistence Hunt Plan

## Techniques
- Registry Run Keys
- Scheduled Tasks
- Services

## High Risk Profile
- Created by user processes
- Executables in temp folders
- Night time creation

## Confidence Scoring
- Low: unusual path
- Medium: unusual path + new binary
- High: system change from office document

## Pseudo Detection
IF registry_change AND creator_process IN ('word.exe','excel.exe')
THEN alert HIGH;
